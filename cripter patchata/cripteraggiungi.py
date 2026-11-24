from cryptography.fernet import Fernet
import json

def cripterAggiungi(password):
    key= Fernet.generate_key()
    f= Fernet(key)
    token=f.encrypt(password.encode())
    return token.hex(), key.hex()

