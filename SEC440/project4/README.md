# Ransomware Project
The files in this project were used in the proof of concept for a ransomware scenario.

### zamsomware.py
This is the ransomware file. The python script generates a random symmetric key in memory that is then used to encrypt file that have a .zam file extension. Encrypted files are given a .getrekt file extension. Then, the symmetric key is encrypted using the attacker's public key and they encrypted symmetric key is stored as a file.

### key_decrypt.py
This file is used to decrypt the symmetric key so that the victim can use it to decrypt their files. The key_decrypt.py file decrypts the symmetric key by using the attacker's private key(since it was encrypted using the attacker's public key). The decrypted symmetric key is output as a file.

### file_decrypt.py
The file_decrypt.py file decrypts the victims encrypted files. It uses the decrypted symmetric key to decrypt files with the ".getrekt" extension(which is the file extension given to the encrypted files). In order for this file to run, the decrypted symmetric key must be present. Once it runs, the files are decrypted
