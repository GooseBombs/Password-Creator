import random
from re import S
from symtable import Symbol
from turtle import st
import string


lower = string.ascii_lowercase
upper = string.ascii_uppercase
number = string.digits
symbol = string.punctuation

hepsi = lower + upper + number + symbol

while True:
    try:
        lenght = random.randint(10,30)
        password = "".join(random.sample(hepsi, lenght))
        print((f"\r{password}"),end="")
    except KeyboardInterrupt:
        
        print((f"\nPrefered Password: {password}"))
        print((f"Password Length: {len(password)}"))
        break