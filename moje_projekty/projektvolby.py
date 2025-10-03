import random
import math

def vypis():
    print("Účást: ", ucast, "%")
    print("ANO:        ", procento[0], "%  ", end="" )
    for i in range(int(procento[0])):
        print("*", end="")
    print("")
    print("SPOLU:      ", procento[1], "%  ", end="" )
    for i in range(int(procento[1])):
        print("*", end="")
    print("")
    print("SPD:        ", procento[2], "%  ", end="" )
    for i in range(int(procento[2])):
        print("*", end="")
    print("")
    print("STAN:       ", procento[3], "%  ", end="" )
    for i in range(int(procento[3])):
        print("*", end="")
    print("")
    print("Piráti:     ", procento[4], "%  ", end="" )
    for i in range(int(procento[4])):
        print("*", end="")
    print("")
    print("Motoristé:  ", procento[5], "%  ", end="" )
    for i in range(int(procento[5])):
        print("*", end="")
    print("")
    print("Stačilo:    ", procento[6], "%  ", end="" )
    for i in range(int(procento[6])):
        print("*", end="")
    print("")
    print("Jiné:       ", procento[7], "%  ", end="" )
    for i in range(int(procento[7])):
        print("*", end="")
    print("")

def odchylka():
    for i in range(8):
        if random.randint(0,1) == 0:
            preference[i] += random.uniform(0.00, 0.02)
        else:
            preference[i] -= random.uniform(0.00, 0.02)




strany = ["ANO", "SPOLU", "SPD", "STAN", "Piráti", "Motoristé", "Stačilo", "Jiné"]
preference = [29.3, 20.5, 13.4, 11.1, 10.0, 6.0, 5.5, 4.2] #0-7
hlasy = [0, 0, 0, 0, 0, 0, 0, 0]
procento = [0, 0, 0, 0, 0, 0, 0, 0]

ucast = round(random.uniform(50, 80), 2)
pocet_hlasicu = 10000000

odchylka()

for i in range(pocet_hlasicu):
    nahoda = round(random.random(), 3) * 100
    for j in range(8):
        if nahoda <= preference[j]:
            hlasy[j] += 1

for i in range(8):
    procento[i] = round((hlasy[i] / pocet_hlasicu) * 100, 2)
    
vypis()

