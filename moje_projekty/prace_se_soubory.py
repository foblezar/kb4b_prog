import random
#cesta = "2. prace_se_soubory\data\studenti.txt"
#
#with open(cesta, "r", encoding="utf-8") as soubor:
#    
#    text = soubor.read()
#    delka = 0
#
#    for line in soubor.split():
#        print(line)
#        delka += 1
#    
#    print("Pocet radku souboru je: ", delka)

cesta = "2. prace_se_soubory\data\citaty.txt"
delka = 0
emoji = ["🌺", "🌼", "🌞", "🐻", "❤️‍", "🔥"]
emoji1 = ["💥", "🔥", "❤️‍", "😎", "🤣"]
pocet_emoji = random.randint(3, 5)


print("Citát dne: ")
for i in range (pocet_emoji):
    print(random.choice(emoji), end=" ")
with open(cesta, "r", encoding="utf=8") as soubor:
    
    text = soubor.read()
    for line in text.split():
        delka += 1
        if delka == (random.randint(1, 7)):
            print(line)

print(random.choice(emoji1))

