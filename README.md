# 📢 Email Text to Voice Conversion 🔊

## 📌 Overview
The **Email Text to Voice Conversion** project is a Python-based utility that reads unread emails from Gmail and converts their content into **Telugu speech** using **Google Text-to-Speech (gTTS)**. This project helps visually impaired users or those who prefer listening to emails instead of reading them.

## 🎯 How It Works
1. 📩 **Fetch Unread Emails** → Connects to Gmail and retrieves unread messages.
2. 🔍 **Extracts Sender & Subject** → Reads the sender's email and the subject line.
3. 🌍 **Translates to Telugu** → Converts the extracted text into **Telugu language**.
4. 🎵 **Plays Audio Output** → Saves the text as an audio file and plays it.

## 🛠️ Technologies & Modules Used
### 1️⃣ **smtplib & imaplib**
   - 📩 Used to connect with Gmail and fetch unread emails securely.

### 2️⃣ **email (MIME Processing)**
   - 📦 Helps parse email content into readable format.

### 3️⃣ **gTTS (Google Text-to-Speech)**
   - 🗣️ Converts extracted email text into **Telugu speech**.

### 4️⃣ **os (Operating System Module)**
   - 📂 Manages audio file creation and playback.

## 🚀 Features
✅ **Automatic Email Retrieval**: Fetches unread emails from the Gmail inbox.
📢 **Voice-Based Email Alerts**: Converts text into an audio file in Telugu.
📩 **Works with Gmail**: Reads emails securely using IMAP.
🎵 **Plays Audio Output**: Reads out sender details and subject.

## 🛠️ Installation & Setup
1️⃣ **Install Dependencies:**
   ```bash
   pip install gtts
   ```
2️⃣ **Set Up Email Configuration:**
   - ✏️ Update `FROM_EMAIL` with your Gmail ID.
   - 🔑 Replace `FROM_PWD` with your **App Password**.

3️⃣ **Run the Script:**  
   ```bash
   python email_to_voice.py
   ```
## 🔗 Project Repository
🔗 [GitHub Repository](https://github.com/vpraneethnadh/Email-to-Voice)
