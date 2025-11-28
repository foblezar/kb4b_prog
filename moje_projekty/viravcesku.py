import csv
import matplotlib.pyplot as plt


cesta = r"2. prace_se_soubory\data\vira_v_cesku.csv"
with open(cesta, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    top_nabozenstvi = 0
    top_nazev_nabozenstvi = ""

    pocet_jedi = 0
    top_jedi = 0
    top_jedi_nazev = "" 

    nazev_viry = []
    pocet_vericich = []


    for line in reader:
        if line["uzemi_txt"] == "Brno":
            if int(line["hodnota"]) > int(top_nabozenstvi):
                top_nabozenstvi = int(line["hodnota"])
                top_nazev_nabozenstvi = line["vira_txt"]

        if line["vira_txt"] == "Jedi" and line["uzemi_txt"] != "Česká republika":
            pocet_jedi += int(line["hodnota"])
            if top_jedi < int(line["hodnota"]):
                top_jedi = int(line["hodnota"])
                top_jedi_nazev = line["uzemi_txt"] 
        
    print(f"{top_nazev_nabozenstvi} : {top_nabozenstvi}")

    print(f"V ČR je {pocet_jedi} jediů, nejvíce v {top_jedi_nazev} ({top_jedi}) ")

 
        if line["uzemi.txt"] == "Česká republika":
            if(int(line["honota"])> 10000):
                nazev_viry.append(line["vira_txt"])
                pocet_vericich.append(int(line["hodnota"]))

    
    plt.bar(nazev_viry, pocet_vericich)
    plt.title("Nabozenstvi v CR")
    plt.show()
