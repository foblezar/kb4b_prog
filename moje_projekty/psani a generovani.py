import random

mini = int(input("Zadej min: ")) 
maxi = int(input("Zadej max: "))
pocet = int(input("Zadej pocet: "))

cesta = "2. prace_se_soubory\data\generovani.txt"
cisla = []
with open(cesta, "w", encoding="utf-8") as file:
    for i in range(pocet):
        cisla.append(random.randint(mini, maxi))

    for i in range(len(cisla)):
        file.write(str(f"{cisla[i]}\n"))


