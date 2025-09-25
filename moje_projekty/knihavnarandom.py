import random
import string

def hod_minci():
    pokracovat = True
    penize = 100
    while pokracovat is True:

        sazka = int(input("Kolik chces vsadit: "))
        penize -= sazka
        tip = input("Tipni si: ")
        hod = random.randint(0, 1)
        if hod == 0:
            padlo = "panna"
        else:
            padlo = "orel"
    
        print("Padlo: ", padlo)

        if tip == padlo:
            print("Vyhravas ", sazka * 2)
            penize += sazka * 2
            print("Stav uctu: ", penize)
        else:
            print ("prohral si")
            print("Stav uctu: ", penize)
        if input("Chces pokracovat [a/n]: ") == "n":
            pokracovat = False

def hod_kostkou():
    pokracovat = True
    soucet = 0
    while pokracovat is True:       
        pocet_kostek = int(input("Zadej pocet kostek: "))
        pocet_sten = int(input("Zadej pocet sten kostky: "))
        print("Hody: ", end="")
        for i in range(pocet_kostek):
            hod = random.randint(1, pocet_sten)
            soucet += hod
            print(hod, end=" ")
        print("Soucet: ", soucet)

def karty_poker():
    kat1 = ["listy", "krize", "srdce", "piky"]
    kat2 = ["eso", "2", "3", "4", "5", "6", "7", "8", "9", "10", "kral", "kralovna", "jan"]

    pokracovat = True

    input("Zadej klavesu pro vygenerovani karty: ")

    val1 = random.choice(kat1)
    val2 = random.choice(kat2)
    print("Vytahl si: ", val1 , "-", val2)
    while pokracovat is True:
        val3 = random.choice(kat1)
        val4 = random.choice(kat2)
        if val3 == val1 and val4 == val2:
            val3 = random.choice(kat1)
            val4 = random.choice(kat2)
        else:
            print("Vytahl si: ", val3 , "-", val4)
            pokracovat = False

def generator_hesla():
    delka = random.randint(7, 12)
    mnozina = [".", ",", "-", "#"]
    heslo = []
    for i in range(delka):
        znak = random.randint(1, 3)

        if znak == 1:
            heslo.append(random.choice(string.ascii_letters)) ###pismena
        if znak == 2:
            heslo.append(random.choice(mnozina))
        if znak == 3:
            heslo.append(random.randint(1, 9))

 ### UDELAT PODMINKU JESTLI SPLNUJE VSECHNY ZNAKY
   # vypsane_heslo = "".join(heslo)
    print("Heslo:", vypsane_heslo)
    
generator_hesla()
