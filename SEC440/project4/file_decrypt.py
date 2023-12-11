from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def decrypt_file(file_path, symmetric_key):
    with open(file_path, 'rb') as file:
        ciphertext = file.read()

    cipher = Cipher(algorithms.AES(symmetric_key), modes.CFB(b'\0' * 16), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    with open(file_path[:-4], 'wb') as decrypted_file:
        decrypted_file.write(plaintext)

def main():
    # Read the decrypted symmetric key from sym_key.dec
    with open('sym_key.dec', 'rb') as sym_key_file:
        symmetric_key = sym_key_file.read()

    # Decrypt all ".zam" files
    for filename in os.listdir('.'):
        if filename.endswith('.getrekt'):
            decrypt_file(filename, symmetric_key)
            os.remove(filename)

if __name__ == "__main__":
    main()
