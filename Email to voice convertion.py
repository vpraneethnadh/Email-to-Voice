# Python 3.8.0
import smtplib
import time
import imaplib
import email
import traceback
from gtts import gTTS
import os

# -------------------------------------------------
#
# Utility to read email from Gmail Using Python
#
# ------------------------------------------------
ORG_EMAIL = "@gmail.com"
FROM_EMAIL = "ecsproject2023" + ORG_EMAIL
FROM_PWD = "fthwnahozzuooxmc"
SMTP_SERVER = "imap.gmail.com"
SMTP_PORT = 993

def read_email_from_gmail():
    try:
        mail = imaplib.IMAP4_SSL(SMTP_SERVER)
        mail.login(FROM_EMAIL,FROM_PWD)
        mail.select('inbox')

        data = mail.search(None, 'UNSEEN')
        mail_ids = data[1]
        id_list = mail_ids[0].split()
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id,first_email_id, -1):
            data = mail.fetch(str(i), '(RFC822)' )
            for response_part in data:
                arr = response_part[0]
                if isinstance(arr, tuple):
                    msg = email.message_from_string(str(arr[1],'utf-8'))
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print('From : ' + email_from + '\n')
                    print('Subject : ' + email_subject + '\n')

                    # Convert output to Telugu using gTTS
                    telugu_text = "నుండి: " + email_from + "\nవిషయం: " + email_subject + "\n"
                    telugu_audio = gTTS(text=telugu_text, lang='te', slow=False)
                    telugu_audio.save("email_telugu.mp3")
                    os.system("mpg123 email_telugu.mp3")  # Play the audio file

    except Exception as e:
        traceback.print_exc()
        print(str(e))

read_email_from_gmail()
