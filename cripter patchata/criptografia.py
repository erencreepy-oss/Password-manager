import json
from cryptography.fernet import Fernet

def cripter(password):
    key= Fernet.generate_key()
    f= Fernet(key)
    token=f.encrypt(password.encode())
    datiVault={
        "chiave": key.hex(),
        "password": token.hex()
    }
    with open("vault.json","w",encoding="utf-8")as file:
        json.dump(datiVault,file, indent=2, ensure_ascii=False)

