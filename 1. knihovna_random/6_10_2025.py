import random


def random_vysledek():
    choice = (random.randint(0, 1))
    if choice == 1: 
            return("orel")

    else:
            return("panna")
        
suma = 100  
kolo = True

while kolo and suma > 0:
    print ("Máš", suma, "Kč")
    sazka = int(input("Kolik chces vsadit?: "))
    tip_uzivatele = input("Zadej orel nebo panna: ")
    print (random_vysledek())

    if tip_uzivatele == random_vysledek():
        print ("Vyhrál jsi")
        suma = suma + (2*sazka)
        print ("Máš", suma, "Kč")
        sazka = int(input("Kolik chces vsadit?: "))
        tip_uzivatele = input("Zadej orel nebo panna: ")
    else:
        print ("Prohrál jsi")
        suma -= sazka
        print ("Máš", suma, "Kč")
        sazka = int(input("Kolik chces vsadit?: "))
        tip_uzivatele = input("Zadej orel nebo panna: ")

    kolo = input("Chces pokracovat? (ano/ne): ") == "ano"
