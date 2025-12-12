import random
import csv
import matplotlib.pyplot as plt

def vypis_statistiky():
    pocet_otazek = 0
    pocet_easy = 0
    pocet_medium = 0
    pocet_hard = 0

    kategorie_gk = 0
    kategorie_eb = 0
    kategorie_ef = 0
    kategorie_em = 0
    kategorie_evg = 0
    kategorie_sn = 0
    kategorie_sc = 0
    kategorie_g = 0
    kategorie_h = 0

    print("Jaký graf chceš vypsat?")
    print("1. Poměr obtížností")
    print("2. Poměr kategorií")
    stat_choice = int(input("Zadej moznost: "))
    if stat_choice == 1:
        with open(r"2. prace_se_soubory\PROJEKT_milionar\quiz_questions.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for line in reader:
                pocet_otazek += 1
                if line["difficulty"] == "easy":
                    pocet_easy += 1
                elif line["difficulty"] == "medium":
                    pocet_medium += 1
                elif line["difficulty"] == "hard":
                    pocet_hard += 1

            difficulties = ["easy", "medium", "hard"]
            pocet_difficulties = [pocet_easy, pocet_medium, pocet_hard]
        plt.bar(difficulties, pocet_difficulties)
        plt.title("Poměr obtížností")
        plt.show()
        print(f"Počet otázek: {pocet_otazek}")
    elif stat_choice == 2:
        with open(r"2. prace_se_soubory\PROJEKT_milionar\quiz_questions.csv", "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for line in reader:
                if line["category"] == "General Knowledge":
                    kategorie_gk += 1
                elif line["category"] == "Entertainment: Books":          
                    kategorie_eb += 1
                elif line["category"] == "Entertainment: Film":          
                    kategorie_ef += 1
                elif line["category"] == "Entertainment: Music":          
                    kategorie_em += 1
                elif line["category"] == "Entertainment: Video Games":           
                    kategorie_evg += 1
                elif line["category"] == "Science: Nature":      
                    kategorie_sn += 1
                elif line["category"] == "Science: Computers":      
                    kategorie_sc += 1
                elif line["category"] == "Geography":
                    kategorie_g += 1
                elif line["category"] == "History":
                    kategorie_h += 1
            
            categories = ["General Knowledge", "Entertaiment: Books", "Entertaiment: Film", "Entertaiment: Music", "Entertaiment: Video Games", "Science: Nature", "Science: Computers", "Geography", "History"]
            pocet_categories = [kategorie_gk, kategorie_eb, kategorie_ef, kategorie_em, kategorie_evg, kategorie_sn, kategorie_sc, kategorie_g, kategorie_h]
        plt.bar(categories, pocet_categories)
        plt.title("Poměr kategorií")
        plt.xticks(rotation=45, ha="right")
        plt.show()



def hlavni_hra():
    
    pokracovat_otazky = True
    easy = 0
    medium = 0
    hard = 0


    with open(r"2. prace_se_soubory\PROJEKT_milionar\quiz_questions.csv", "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        otazky = list(reader)         #pole s dictionary jako otazky
        print()
        print("Obtížnost - easy")
        while pokracovat_otazky == True:
            otazka = otazky[random.randint(0, 259)]
            
            if otazka["difficulty"] == "easy":
                print()
                print(otazka["question"])
                print()
                
                odpoved = input("Zadej odpoved: [True/False]: ")
                if odpoved != otazka["correct_answer"]:
                    print("Odpovedel si spatne! ")
                    print(f"Zodpovedel si [{easy} / 15] otazek")
                    break
                
                easy += 1
                
                if easy == 5:
                    pokracovat_otazky = False

        if easy == 5:
            pokracovat_otazky = True
            print()
            print("Obtížnost - medium")
            while pokracovat_otazky == True:
                otazka = otazky[random.randint(0, 259)]
                if otazka["difficulty"] == "medium":
                    print()
                    print(otazka["question"])
                    print()

                    odpoved = input("Zadej odpoved: [True/False]: ")
                    if odpoved != otazka["correct_answer"]:
                        print("Odpovedel si spatne! ")
                        print(f"Zodpovedel si [{medium+5} / 15] otazek")
                        break
                    
                    medium += 1

                    if medium == 5:
                        pokracovat_otazky = False

        if medium == 5:
            pokracovat_otazky = True
            print()
            print("Obtížnost - hard")
            while pokracovat_otazky == True:
                otazka = otazky[random.randint(0, 259)]
                if otazka["difficulty"] == "hard":
                    print()
                    print(otazka["question"])
                    print()

                    odpoved = input("Zadej odpoved: [True/False]: ")
                    if odpoved != otazka["correct_answer"]:
                        print("Odpovedel si spatne! ")
                        print(f"Zodpovedel si [{hard+5} / 15] otazek")
                        break
                    
                    hard += 1
                    
                    if hard == 5:
                        print("Vyhrál si! ")
                        zapsani_vyherce()
                        pokracovat_otazky = False


def zapsani_vyherce():
    cesta = r"2. prace_se_soubory\PROJEKT_milionar\vyherci.txt"
    with open(cesta, "a", encoding="utf-8") as file:
        zprava = input("Zadej svoji zpravu: ")
        file.write(str(f"{uzivatel} - {zprava}\n"))

def vypsani_vyhercu():
    cesta = r"2. prace_se_soubory\PROJEKT_milionar\vyherci.txt"
    print("Vyherci: ")
    with open(cesta, "r", encoding="utf-8") as file:
       lines = file.readlines()
       for line in lines:
           print(line)


def main_menu():
    pokracovat = True
    while pokracovat is True:
        print("1. Statistiky otazek")
        print("2. Vypis vsech vitezu")
        print("3. Hrat hru")
        print("0. Ukončit hru")
        choice = int(input("Zadej moznost: "))
        if choice == 1:
            vypis_statistiky()
        elif choice == 2:
            vypsani_vyhercu()
        elif choice == 3:
            hlavni_hra()
        else:
            pokracovat = False




success = 0

print("Zadej zpusob prihlaseni: ")
print("1. Registrace")
print("2. Prihlaseni")
choice = int(input("Zadej moznost: "))
if choice == 1:
    login = input("Zadej login: ")
    password = input("Zadej password: ")
    with open(r"2. prace_se_soubory\PROJEKT_milionar\logins.txt", "a", encoding="utf-8") as file:
        file.write(str(f"{login} {password}\n"))
        success = 1

elif choice == 2:
    login = input("Zadej login: ")
    password = input("Zadej password: ")
    with open(r"2. prace_se_soubory\PROJEKT_milionar\logins.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        for line in lines:
            control_login = line.split()
            if login == control_login[0] and password == control_login[1]:
                print()
                print("Přihlášení úspěšné")
                print()
                success = 1
                uzivatel = login
   
if success == 1:
    main_menu()
else:
    print("Neúspěšné přihlášení")
