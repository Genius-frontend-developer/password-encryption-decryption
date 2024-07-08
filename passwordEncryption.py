# Password Encryption Programm

import base64


def passEncryption(password):
    encoded_bytes = base64.b64encode(password.encode())
    print(f"Encoded password with base64: {encoded_bytes}")

user_password = input("Enter your password: ")
passEncryption(user_password)
