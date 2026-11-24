from cryptography.fernet import Fernet
import json
import hmac

def controlloPasswordIniziale(password2):
    with open("vault.json")as file:
        dati=json.load(file)

    f=Fernet(bytes.fromhex(dati["chiave"]))
    passwordOriginale= f.decrypt(bytes.fromhex(dati["password"])).decode()

    if hmac.compare_digest(password2, passwordOriginale):
        print("Access allowed ")
        return True
    else:
        print("Access denied ")
        return False



