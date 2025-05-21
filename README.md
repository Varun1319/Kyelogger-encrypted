#  Encrypted Keylogger (Ethical Malware Simulation)

A Python-based keylogger for **ethical research and malware analysis**, featuring **AES encryption** and **email alerts**.The **secret.key** file contains the AES encryption key (generated using the cryptography library's Fernet module), which is used to encrypt and decrypt the keystroke logs.
This key is:

- Randomly generated using Fernet.generate_key()

- Used to both encrypt and decrypt data (symmetric AES encryption)

- Saved to disk so your keylogger and decryptor can reuse it consistently



##  Legal Disclaimer

This tool is intended for **educational and ethical use only**.  
Do **not** use this on any system without **explicit permission**.  


##  Features

- Keystroke logging (using `pynput`)
- AES encryption (via `cryptography.Fernet`)
- Automatic email reports (base64-encoded)
- Stealth mode via `pythonw` or `--noconsole`
- Optional local decryption script
  

##  Setup

1. Clone this repo
2. Install dependencies: *pip install -r requirements.txt*
3. Edit *keylogger_encrypted.py* to configure:
   *EMAIL_ADDRESS = "youremail@gmail.com"
    EMAIL_PASSWORD = "your_app_password"*
4. Run safely in a VM: *python keylogger_encrypted.py*
5. Use *decrypt_logs.py* to view encrypted log contents: *python decrypt_logs.py*



