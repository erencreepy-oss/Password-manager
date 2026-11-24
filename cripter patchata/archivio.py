import json
import os
from cryptography.fernet import Fernet
from cripteraggiungi import cripterAggiungi
import sys

fileDati= "archivio.json"

def salva(dati):
    with open(fileDati,"w", encoding="utf-8") as file:
        json.dump(dati, file, indent=2, ensure_ascii=False)

def carica():
    if not os.path.exists(fileDati):
        return []
    with open(fileDati, encoding="utf-8") as file:
        return json.load(file)

def aggiungi(dati):
        sito=input("Set the site ").strip()
        utente=input("Set the username ").strip()
        passw=input("Set the password ")
        passwC,key=cripterAggiungi(passw)

        if sito=="":
            print("ERROR:No site was specified ")
        elif utente=="":
            print("ERROR:No username was specified ")
        elif passw=="":
            print("ERROR:No password was specified ")
        else:
            esiste=False
            for voce in dati:
                if voce["sito"].lower()==sito.lower() and voce["utente"]==utente:
                    esiste=True
                    break
            if esiste:
                    print("Esiste gia una voce per quel utente in quel sito")
            else:
                dati.append({"sito": sito, "utente": utente, "password": passwC, "key": key})
                salva(dati)
                

def elenca():
    with open(fileDati)as file:
        tutto=json.load(file)
    
    for i,elemento in enumerate(tutto, start=1):
        passBytes=bytes.fromhex(elemento["password"])
        keyBytes=bytes.fromhex(elemento["key"])

        f=Fernet(keyBytes)
        passwordDecriptata= f.decrypt(passBytes).decode()
        print(i,"Site:",elemento["sito"],"Username:",elemento["utente"],"Password:", passwordDecriptata)

def cerca():
    with open(fileDati)as file:
        tutto=json.load(file)
        ricerca=input("What do you want to search(write a saved site) ").strip().lower()
        risultati=[
            item for item in tutto
            if any(ricerca in str(valore).lower() for valore in item.values())
        ]
        for i,elemento in enumerate(risultati, start=1):
                passBytes=bytes.fromhex(elemento["password"])
                keyBytes=bytes.fromhex(elemento["key"])
        
                f=Fernet(keyBytes)
                passwordDecriptata= f.decrypt(passBytes).decode()
        if not risultati==[]:
            for r in range(len(risultati)):
                print("Site:",risultati[r]["sito"],"Username:",risultati[r]["utente"],"Password:",passwordDecriptata)
        else:
            print("Doesn't exist")


def cancella():
    with open(fileDati)as file:
        tutto=json.load(file)
        for i,elemento in enumerate(tutto, start=1):
            passBytes=bytes.fromhex(elemento["password"])
            keyBytes=bytes.fromhex(elemento["key"])
        
            f=Fernet(keyBytes)
            passwordDecriptata= f.decrypt(passBytes).decode()
        for i, item in enumerate(tutto, start=1):
            print(i, "Site",item["sito"], "Username",item["utente"], "Password",passwordDecriptata)
        try:
            scelta=int(input("Which one do you want to delete? "))
            if scelta <= len(tutto):
                eliminato= tutto.pop(scelta-1)
                with open(fileDati,"w", encoding="utf-8")as f:
                    json.dump(tutto,f,indent=2, ensure_ascii=False)
                print("DELETED ", "Site:",eliminato["sito"], "Username:",eliminato["utente"], "Password:",passwordDecriptata)
            else:
                print("Number not in the list ")
        except ValueError:
            print("You have to digit an integer number ")

def esci():
    sys.exit()


with open(fileDati, "r", encoding="utf-8") as file:
    dati = json.load(file)



