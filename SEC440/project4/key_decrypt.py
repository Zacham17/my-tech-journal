from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

def decrypt_symmetric_key(encrypted_key_path, private_key_path):
    with open(private_key_path, 'rb') as file:
        private_key = serialization.load_pem_private_key(file.read(), password=None, backend=default_backend())

    with open(encrypted_key_path, 'rb') as file:
        encrypted_key = file.read()

    decrypted_key = private_key.decrypt(
        encrypted_key,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    with open('sym_key.dec', 'wb') as sym_key_file:
        sym_key_file.write(decrypted_key)

def main():
    # Assuming the private key is stored in a file called "private_key.pem"
    decrypt_symmetric_key('sym_key.enc', 'private_key.pem')

if __name__ == "__main__":
    main()
