import tkinter as tk
from googletrans import Translator
from gtts import gTTS
import os
import shutil
from pathlib import Path

def translate_and_speak():
    # Hide notification label
    notification_label.place_forget()
    
    # Translate text to Thai
    text = text_entry.get()
    translator = Translator()
    translated_text = translator.translate(text, src='th', dest='th').text
    
    # Generate speech from translated text
    tts = gTTS(text=translated_text, lang='th')
    filename = f"{translated_text}.mp3"  # Use text as filename
    tts.save(filename)
    
    # Get the download folder path
    download_folder = str(Path.home() / "Downloads")
    
    # Move the audio file to the download folder
    shutil.move(filename, os.path.join(download_folder, filename))
    
    # Notify user about the file location
    notification_label.config(text=f"ไฟล์เสียงถูกบันทึกที่: {download_folder}")
    notification_label.place(relx=0.5, rely=0.8, anchor="center")
    
    # After 5 seconds, clear the notification
    root.after(5000, clear_notification)

def clear_notification():
    notification_label.config(text="")
    notification_label.place_forget()

# Function to paste text using Ctrl + V
def paste_text(event):
    text = root.clipboard_get()
    text_entry.insert(tk.INSERT, text)

# Create GUI window
root = tk.Tk()
root.title("กูเกิล แปลงคำเป็นเสียง")
root.geometry("500x300")
root.resizable(False, False)  # Disable resizing

# Set icon for the GUI window
icon = tk.PhotoImage(file='W:\\translate\\icon.png')
root.iconphoto(False, icon)

# Load background image
image = tk.PhotoImage(file="W:\\translate\\background.png")
background_label = tk.Label(root, image=image)
background_label.place(relwidth=1, relheight=1)

# Create text entry box
text_entry = tk.Entry(root, width=40, font=("Helvetica", 14), borderwidth=2, relief="solid")
text_entry.place(relx=0.5, rely=0.4, anchor="center")

# Create "Translate" button
translate_button = tk.Button(root, text="แปลง", command=translate_and_speak, font=("Helvetica", 12), bg="#4CAF50", fg="white", borderwidth=2, relief="solid")
translate_button.place(relx=0.5, rely=0.6, anchor="center")

# Label to display notification
notification_label = tk.Label(root, text="", font=("Helvetica", 10), fg="green")
notification_label.place(relx=0.5, rely=0.8, anchor="center")

# Bind paste_text function to Ctrl + V
root.bind("<Control-v>", paste_text)

# Start GUI
root.mainloop()
