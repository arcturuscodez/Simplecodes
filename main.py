import random
import string
import socket
import os
from cryptography.fernet import Fernet

def generate_encryption_key():
    return Fernet.generate_key()

def save_encryption_key(key):
    folder_name = "encryption_folder"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    key_file = os.path.join(folder_name, "encryption_key.txt")
    with open(key_file, "wb") as file:
        file.write(key)

    print("Encryption key saved successfully!")

def load_encryption_key():
    folder_name = "encryption_folder"
    key_file = os.path.join(folder_name, "encryption_key.txt")
    if os.path.exists(key_file):
        with open(key_file, "rb") as file:
            return file.read()
    return None

def encrypt_data(key, data):
    f = Fernet(key)
    return f.encrypt(data.encode()).decode()

def decrypt_data(key, encrypted_data):
    f = Fernet(key)
    return f.decrypt(encrypted_data.encode()).decode()

def generate_passcode(length=12):
    chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def save_credentials(account_name, encrypted_username, encrypted_password):
    folder_name = "passcode_folder"
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    filename = f"{account_name}.txt"
    file_path = os.path.join(folder_name, filename)
    with open(file_path, "w") as file:
        file.write(f"Account Name: {account_name}\n")
        file.write(f"Encrypted Username: {encrypted_username}\n")
        file.write(f"Encrypted Password: {encrypted_password}\n")

    print("Credentials saved successfully!")

def encrypt_passcodes_folder():
    encryption_key = load_encryption_key()
    if encryption_key:
        folder_name = "passcode_folder"
        for root, dirs, files in os.walk(folder_name):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, "rb") as file:
                    data = file.read()
                f = Fernet(encryption_key)
                encrypted_data = f.encrypt(data)
                with open(file_path, "wb") as file:
                    file.write(encrypted_data)
        print("Passcodes folder encrypted successfully.")
    else:
        print("Encryption key not found.")

def decrypt_passcodes_folder():
    encryption_key = load_encryption_key()
    if encryption_key:
        folder_name = "passcode_folder"
        for root, dirs, files in os.walk(folder_name):
            for file in files:
                file_path = os.path.join(root, file)
                with open(file_path, "rb") as file:
                    encrypted_data = file.read()
                f = Fernet(encryption_key)
                decrypted_data = f.decrypt(encrypted_data)
                with open(file_path, "wb") as file:
                    file.write(decrypted_data)
        print("Passcodes folder decrypted successfully.")
    else:
        print("Encryption key not found.")

def generate_encryption_key_command():
    encryption_key = generate_encryption_key()
    save_encryption_key(encryption_key)

def generate_credentials():
    account_name = input("Enter the account name: ")
    encryption_key = load_encryption_key()
    if encryption_key:
        username = generate_passcode(8)
        password = generate_passcode(12)
        encrypted_username = encrypt_data(encryption_key, username)
        encrypted_password = encrypt_data(encryption_key, password)
        save_credentials(account_name, encrypted_username, encrypted_password)
    else:
        print("Encryption key not found.")

def main():

    while True:
        print("Enter '1' to generate credentials, '2' to encrypt the passcodes folder, '3' to decrypt the passcodes folder, '4' to generate a new encryption key, or '0' to exit:")
        choice = input()
        if choice == '1':
            generate_credentials()
        elif choice == '2':
            encrypt_passcodes_folder()
        elif choice == '3':
            decrypt_passcodes_folder()
        elif choice == '4':
            generate_encryption_key_command()
        elif choice == '0':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()