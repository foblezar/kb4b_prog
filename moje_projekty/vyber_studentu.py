import random


def vyber_studentu(n):
    cesta = "2. prace_se_soubory\data\studenti.txt"
    with open(cesta, "r", encoding="utf-8") as file:
        radky = file.readlines()
      
    jmena = []

    for i in range(len(radky)):
        jmena.append(radky[i].strip())  #stacilo radky[i] = radky[i].strip()

    for i in range(n):
        print(jmena[random.randint(0, len(jmena)-1)]) #xxxx.sort()

n = int(input("Zadej pocet studentu: "))   

vyber_studentu(n)







