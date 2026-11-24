import secrets
import string

def generatore(lunghezza):
    caratteri= string.ascii_letters+ string.digits+"!@#$%&*?"
    return "".join(secrets.choice(caratteri) for _ in range (lunghezza))
