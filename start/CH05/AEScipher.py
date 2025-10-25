# AES Encryption and Decryption
#By Terrance Blandford


import os
from base64 import b64encode, b64decode
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

key = os.urandom(16)
iv = os.urandom(16)
print(f"Generated AES Key (base64): {b64encode(key).decode()}")

plaintext = input("Enter a plaintext message: ")

padder = padding.PKCS7(128).padder()
padded = padder.update(plaintext.encode()) + padder.finalize()

cipher = Cipher(algorithms.AES(key), modes.CBC(iv))
encryptor = cipher.encryptor()
ciphertext = encryptor.update(padded) + encryptor.finalize()


ct_b64 = b64encode( iv + ciphertext).decode()
print(f"Encrypted message: {ct_b64}")

data = b64decode(ct_b64)
iv2, ct2 = data[:16], data[16:]
cipher2 = Cipher(algorithms.AES(key), modes.CBC(iv2))
decryptor = cipher2.decryptor()
plain_padded = decryptor.update(ct2) + decryptor.finalize()

unpadder = padding.PKCS7(128).unpadder()
decrypted = unpadder.update(plain_padded) +unpadder.finalize()
print(f"Decrypted message: {decrypted.decode()}")