import random

#def hod_dvema_kostkami():
#    kostka1 = 0
#    kostka2 = 0
#    pocet_hodu = 0
#
#    pokracovat = True
#
#    while pokracovat is True:
#        kostka1 = random.randint(1, 6)
#        kostka2 = random.randint(1, 6)
#
#        print(kostka1, ",", kostka2)
#
#        pocet_hodu += 1
#
#        if kostka1 == kostka2:
#
#            print("Padla dvojice: ", kostka1, ",", kostka2)
#            print("Počet hodu: ", pocet_hodu)
#
#            pokracovat = False
#        
#    return kostka1, kostka2
#
#hod_dvema_kostkami()
#def vypis_statistiky(temps):
#    soucet = 0
#    prumer = 0
#    pocet = 0
#    for prvek in temps:
#        print(prvek, end=" ")
#    
#    for prvek in temps:
#        soucet += prvek
#        prumer = soucet / 24
#        prumer = round(prumer, 3)
#    print()
#    print("Prumerna teplota: ", prumer, "C")
#
#    for prvek in temps:
#        if prvek < 0:
#            pocet += 1
#    print("Pocet mereni pod bodem mrazu: ", pocet)
#
#temps = []
#for i in range(24):
#    temps.append(random.randint(-10, 20))
#vypis_statistiky(temps)

def generuj_priklad():
    y = random.randint(1, 100)

    mocnina = y*y
    print("Uhodni odmocninu cisla: ", mocnina)

    x = int(input("Zadej cislo: "))

    if x == y:
        return True
    else:
        return False


spravne = 0
for i in range(3):    
    if generuj_priklad() == True:
        spravne +=1

print("Spravne: ", spravne, end="")
print("/3")

    

