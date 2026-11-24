import os
import json
from criptografia import cripter
from generatorePassword import generatore
from controllopasswordiniziale import controlloPasswordIniziale
from archivio import aggiungi
from archivio import elenca
from archivio import cerca
from archivio import cancella
from archivio import esci

if os.path.exists("vault.json"):
    controlloPasswordIniziale(input("Inserisci la password "))
else:    
    print("---------------SET YOUR PASSWORD---------------")
    decidione1=input("Do you want to set the password yourself or generate one?(set/generate): ").lower()
    if decidione1=="set":
        password=input("Set the password ")
        cripter(password)
    else:
        lunghezza=int(input("Set the desired length "))
        password=generatore(lunghezza)
        print(password)
        cripter(password)
    controlloPasswordIniziale(input("Set the password again "))

while True:
    print("1) Add  2) list  3) Search  4) Delete  5) Exit")
    scelta = input("> ").strip()
    if scelta=="1":
        with open("archivio.json", "r", encoding="utf-8") as file:
            dati = json.load(file)
        aggiungi(dati)
    elif scelta =="2":
        elenca()
    elif scelta=="3":
        cerca()
    elif scelta=="4":
        cancella()
    elif scelta=="5":
        esci()
    else:
        print("ERROR: none of the listed possibilities was indicated ")








