# Password Decryption Programm
import base64

def passwordDec(password):
    decode_bytes = base64.b64decode(password)
    decoded_bytes = decode_bytes.decode()
    print(f"Decoded password: {decoded_bytes}")

user_password = input("Enter the encrypted password with base64:  ")
passwordDec(user_password)