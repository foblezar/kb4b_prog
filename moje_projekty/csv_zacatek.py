import csv
import matplotlib.pyplot as plt


cesta = r"2. prace_se_soubory\data\teploty.csv"
with open(cesta, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    roky = []
    teploty = []


    max_teplota = 0
    max_rok = 0

    for line in reader:
        if (line["TIME"] == "AVG"):
            teplota = float(line["TEMPERATURE"])
            teploty.append(teplota)
            roky.append(line["YEAR"])

        if (teplota > max_teplota):
            max_teplota = teplota
            max_rok = line["YEAR"]

    print(f"Nejvyssi teplota: {max_teplota} v roce {max_rok}")

   
    plt.plot(roky, teploty)
    plt.title("Prumerne hodnoty v CR")
    plt.xlabel("Roky")
    plt.ylabel("Teploty")
    plt.xticks(roky[::5])
    plt.show()