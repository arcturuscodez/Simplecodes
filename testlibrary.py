from main import *

class testlibrary:
    def __init__(self):
        self.encryption_key = None

    def generate_and_save_encryption_key(self):
        self.encryption_key = generate_encryption_key()
        save_encryption_key(self.encryption_key)

    def load_encryption_key(self):
        self.encryption_key = load_encryption_key()

    def generate_credentials(self, account_name):
        if self.encryption_key:
            username = generate_passcode(8)
            password = generate_passcode(12)
            encrypted_username = encrypt_data(self.encryption_key, username)
            encrypted_password = encrypt_data(self.encryption_key, password)
            save_credentials(account_name, encrypted_username, encrypted_password)
        else:
            raise Exception("Encryption key not found.")
        
    def access_credentials(self, account_name):
        if self.encryption_key:
            # Load the saved credentials
            folder_name = "passcode_folder"
            filename = f"{account_name}.txt"
            file_path = os.path.join(folder_name, filename)
            with open(file_path, "r") as file:
                lines = file.readlines()
            encrypted_username = lines[1].split(": ")[1].strip()
            encrypted_password = lines[2].split(": ")[1].strip()

            # Try to decrypt the saved credentials
            try:
                username = decrypt_data(self.encryption_key, encrypted_username)
                password = decrypt_data(self.encryption_key, encrypted_password)
            except:
                raise Exception("Failed to access saved credentials.")
        else:
            raise Exception("Encryption key not found.")