from datetime import datetime


def zprava():
    username = input("Zadej jmeno: ")
    if username == "konec":
            return False, False, False
    message = input("Zprava: ")
    datum = datetime.now()
    return username, message, datum

cesta = "2. prace_se_soubory\data\chatlog.txt"
pokracovat = True


while pokracovat is True:
    with open(cesta, "a", encoding="utf-8") as file:
        username, message, datum = zprava()
        if username == False:
            pokracovat = False
            break
        file.write(f"{datum} - {username}: {message}\n")



