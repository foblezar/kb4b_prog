import random

def generuj_priklad():
    cislo1 = random.randint(0, 100)
    op = random.choice(["+", "-", "*"])
    cislo2 = random.randint(0, 100)

    print(f"{cislo1} {op} {cislo2} = ")
    vstup = int(input())

    if op == "+":
        spravne = cislo1 + cislo2
    elif op == "-":
        spravne = cislo1 - cislo2
    elif op == "*":
        spravne = cislo1 * cislo2
    
    return vstup == spravne

spravne = 0
for i in range(3):    
    if generuj_priklad() == True:
        spravne +=1

print("Spravne: ", spravne, end="")
print("/3")