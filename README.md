# 📧 Email Text to Voice Conversion 🔊

## 📌 Overview
The **Email Text to Voice Conversion** project is designed to enhance email accessibility by converting email content into **speech**. This is particularly useful for visually impaired individuals or anyone who prefers listening to their emails instead of reading. The system fetches unread emails, extracts key information, and converts the content into **Telugu audio output** using **Google Text-to-Speech (gTTS)**.

## 🎯 How It Works
1. 📥 **Fetch Unread Emails** → The system connects to a Gmail inbox and retrieves unread emails.
2. 📨 **Extract Email Details** → Reads the sender's address and subject line.
3. 🗣️ **Convert to Telugu Audio** → Uses **gTTS** to convert the extracted text into a Telugu voice message.
4. 🔊 **Play the Audio Output** → Automatically plays the generated audio file.

## 🛠️ Technologies and Modules Used
### 1️⃣ **imaplib & email**
   - 📬 Handles email fetching from a Gmail inbox.
   - 📩 Parses email content (sender and subject).

### 2️⃣ **gTTS (Google Text-to-Speech)**
   - 🗣️ Converts text into speech.
   - 🎵 Supports multiple languages, including **Telugu**.

### 3️⃣ **smtplib**
   - 📤 Manages SMTP authentication and email handling.

### 4️⃣ **os & mpg123**
   - 🖥️ Handles file management.
   - 🔊 Plays the generated audio output.

## 🚀 Features
✅ **Automated Email Retrieval**: Fetches unread emails from the inbox.  
✅ **Text-to-Speech in Telugu**: Converts email content into an audible format.  
✅ **Real-Time Playback**: Plays the generated speech file instantly.  
✅ **Simple & Lightweight**: Uses Python libraries for efficient performance.  

## 🛠️ Installation & Setup
1️⃣ **Install Dependencies:**
   ```bash
   pip install gtts
   ```
2️⃣ **Set Up Email Configuration:**
   - ✏️ Update `FROM_EMAIL` with your Gmail ID.
   - ✏️ Update `FROM_PWD` with your email's app password.
3️⃣ **Run the Script:**
   ```bash
   python email_to_voice.py
   ```

## 🔗 GitHub Repository
🔗 **Project Repository:** [Email-to-Voice](https://github.com/vpraneethnadh/Email-to-Voice)
