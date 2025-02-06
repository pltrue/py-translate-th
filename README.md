# 🎤 Py-Translate-TH

โปรแกรม GUI สำหรับแปลข้อความเป็นภาษาไทยและแปลงข้อความเป็นเสียงพูด โดยใช้ `googletrans` หรือ `deep-translator` และ `gTTS` พร้อมติดตั้งไลบรารีให้อัตโนมัติหากยังไม่มี

![py-translate-th](https://github.com/twoza0123/py-translate-th/assets/93757631/4a8cc84d-d93f-445d-ae7b-74e4d6dc2ec4)

---

## 📌 คุณสมบัติ
✅ แปลข้อความเป็นภาษาไทยอัตโนมัติ (รองรับ `googletrans` และ `deep-translator`)
✅ แปลงข้อความเป็นเสียงพูดด้วย `gTTS`
✅ บันทึกไฟล์เสียงลงในโฟลเดอร์ `Downloads`
✅ มี GUI ใช้งานง่ายผ่าน `tkinter`
✅ ติดตั้งไลบรารีอัตโนมัติ หากยังไม่มี
✅ รองรับ `Ctrl + V` สำหรับวางข้อความ

---

## 🚀 วิธีติดตั้งและใช้งาน

### 1️⃣ ติดตั้ง Python (ถ้ายังไม่มี)
- ดาวน์โหลดและติดตั้ง Python ได้จาก [python.org](https://www.python.org/downloads/)

### 2️⃣ ดาวน์โหลดโปรเจกต์

```sh
# Clone โปรเจกต์ผ่าน Git
git clone https://github.com/twoza0123/py-translate-th.git
cd py-translate-th
```

หรือ ดาวน์โหลด ZIP และแตกไฟล์

### 3️⃣ รันโปรแกรม

```sh
python main.py
```

> 🔹 โปรแกรมจะติดตั้งไลบรารีอัตโนมัติหากยังไม่มี และเปิด GUI ให้ใช้งานทันที!

---

## 🛠️ ไลบรารีที่ใช้

- `googletrans==4.0.0-rc1` – ใช้แปลข้อความ (ถ้ามีปัญหา ใช้ `deep-translator` แทน)
- `deep-translator` – ตัวเลือกสำรองสำหรับแปลภาษา
- `gtts` – แปลงข้อความเป็นเสียง
- `tkinter` – สร้าง GUI สำหรับผู้ใช้

---

## 🖼️ ภาพตัวอย่าง

![UI Screenshot](https://github.com/twoza0123/py-translate-th/assets/93757631/4a8cc84d-d93f-445d-ae7b-74e4d6dc2ec4)

---

## 📜 License
โปรเจกต์นี้อยู่ภายใต้ MIT License

---

## 🧑‍💻 ผู้พัฒนา
**[twoza0123](https://github.com/twoza0123/)** – พัฒนาและดูแลโค้ด

หากมีข้อเสนอแนะ สามารถเปิด Issue หรือ Pull Request ได้เลย 🎉
