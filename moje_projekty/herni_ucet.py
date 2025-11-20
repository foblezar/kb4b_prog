import random

def vytvoreni_uctu():
    login = input("Zadej jmeno: ")
    heslo = input("Zadej heslo: ")



print("Vyber moznost")
print("1. Vytvoreni uctu")
print("2. Zustatek")
print("3. Hod minci")
choice = int(input("Vyber moznost: "))
if choice == 1:
    vytvoreni_uctu()