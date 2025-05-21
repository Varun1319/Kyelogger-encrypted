from cryptography.fernet import Fernet

def load_key():
    return open("secret.key", "rb").read()

def decrypt_log(file_path):
    key = load_key()
    with open(file_path, "rb") as file:
        encrypted_data = file.read()
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_data)
    return decrypted.decode()

if __name__ == "__main__":
    file_path = input("Enter path to encrypted log: ")
    try:
        print(decrypt_log(file_path))
    except Exception as e:
        print(f"Decryption failed: {e}")
