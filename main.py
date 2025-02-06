import os
import sys
import subprocess

# ฟังก์ชันติดตั้งไลบรารี
def install_package(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

# ตรวจสอบและติดตั้งไลบรารีที่จำเป็น
required_packages = ["gtts", "googletrans==4.0.0-rc1", "deep-translator"]
for package in required_packages:
    try:
        __import__(package.split("==")[0])  # ตรวจสอบเฉพาะชื่อแพ็กเกจหลัก
    except ImportError:
        print(f"กำลังติดตั้ง {package} ...")
        install_package(package)

# นำเข้าไลบรารีหลังติดตั้ง
import tkinter as tk
import shutil
from pathlib import Path
from gtts import gTTS

# ตรวจสอบไลบรารีแปลภาษา
try:
    from googletrans import Translator
    translator = Translator()
    def translate_text(text):
        return translator.translate(text, src='auto', dest='th').text
except ModuleNotFoundError:
    from deep_translator import GoogleTranslator
    translator = GoogleTranslator(source='auto', target='th')
    def translate_text(text):
        return translator.translate(text)

def translate_and_speak():
    notification_label.place_forget()
    text = text_entry.get()
    translated_text = translate_text(text)

    tts = gTTS(text=translated_text, lang='th')
    filename = "translated_audio.mp3"
    tts.save(filename)

    download_folder = str(Path.home() / "Downloads")
    shutil.move(filename, os.path.join(download_folder, filename))

    notification_label.config(text=f"ไฟล์เสียงถูกบันทึกที่: {download_folder}")
    notification_label.place(relx=0.5, rely=0.8, anchor="center")
    root.after(5000, clear_notification)

def clear_notification():
    notification_label.config(text="")
    notification_label.place_forget()

def paste_text(event):
    text = root.clipboard_get()
    text_entry.insert(tk.INSERT, text)

script_dir = Path(__file__).parent
icon_path = script_dir / "icon.png"
background_path = script_dir / "background.png"

root = tk.Tk()
root.title("แปลงคำเป็นเสียง")
root.geometry("500x300")
root.resizable(False, False)

if icon_path.exists():
    icon = tk.PhotoImage(file=str(icon_path))
    root.iconphoto(False, icon)

if background_path.exists():
    image = tk.PhotoImage(file=str(background_path))
    background_label = tk.Label(root, image=image)
    background_label.place(relwidth=1, relheight=1)

text_entry = tk.Entry(root, width=40, font=("Helvetica", 14), borderwidth=2, relief="solid")
text_entry.place(relx=0.5, rely=0.4, anchor="center")

translate_button = tk.Button(root, text="แปลง", command=translate_and_speak, font=("Helvetica", 12), bg="#4CAF50", fg="white", borderwidth=2, relief="solid")
translate_button.place(relx=0.5, rely=0.6, anchor="center")

notification_label = tk.Label(root, text="", font=("Helvetica", 10), fg="green")
notification_label.place(relx=0.5, rely=0.8, anchor="center")

root.bind("<Control-v>", paste_text)
root.mainloop()
