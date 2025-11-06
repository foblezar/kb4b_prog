cesta = "2. prace_se_soubory\data\slova.txt"
with open(cesta, "r", encoding="utf-8") as file:
    radky = file.readlines()
    
soucet = 0    

for i in range(len(radky)):
    radek = radky[i].strip() 
    print(radky[i].strip())
    print(len(radky[i].strip()))
    soucet += len(radky[i].strip())
                
print(soucet)


