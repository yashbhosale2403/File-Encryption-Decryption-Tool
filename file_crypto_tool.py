from cryptography.fernet import Fernet

# Generate and save a key
def generate_key():
    return Fernet.generate_key()

def save_key(key, filename='secret.key'):
    with open(filename, 'wb') as f:
        f.write(key)

def load_key(filename='secret.key'):
    try:
        with open(filename, 'rb') as f:
            return f.read()
    except FileNotFoundError:
        print("Key file not found.")
        return None

# Encryption
def encrypt_file(input_file, output_file, key):
    try:
        fernet = Fernet(key)
        with open(input_file, 'rb') as f:
            data = f.read()
        encrypted = fernet.encrypt(data)
        with open(output_file, 'wb') as f:
            f.write(encrypted)
        print(f"✅ Encrypted and saved to: {output_file}")
    except Exception as e:
        print(f"❌ Encryption failed: {e}")

# Decryption
def decrypt_file(input_file, output_file, key):
    try:
        fernet = Fernet(key)
        with open(input_file, 'rb') as f:
            encrypted_data = f.read()
        decrypted = fernet.decrypt(encrypted_data)
        with open(output_file, 'wb') as f:
            f.write(decrypted)
        print(f"✅ Decrypted and saved to: {output_file}")
    except Exception as e:
        print(f"❌ Decryption failed: {e}")

# Menu
def main():
    print("=== 🔐 File Encryption/Decryption Tool ===")
    print("1. Generate and save a new key")
    print("2. Encrypt a file")
    print("3. Decrypt a file")
    choice = input("Choose an option (1/2/3): ").strip()

    if choice == '1':
        key = generate_key()
        save_key(key)
        print("🔑 New key saved as 'secret.key'.")

    elif choice == '2':
        key = load_key()
        if not key:
            return
        input_file = input("Enter path of the file to encrypt: ").strip()
        output_file = input("Enter name for encrypted output file: ").strip()
        encrypt_file(input_file, output_file, key)

    elif choice == '3':
        key = load_key()
        if not key:
            return
        input_file = input("Enter path of the encrypted file: ").strip()
        output_file = input("Enter name for decrypted output file: ").strip()
        decrypt_file(input_file, output_file, key)

    else:
        print("❌ Invalid option.")

if __name__ == "__main__":
    main()
