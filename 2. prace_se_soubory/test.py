import csv
import matplotlib.pyplot as plt

cesta = r"2. prace_se_soubory\data\vira_v_cesku.csv"

with open(cesta, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    mesto = []
    item = {}     
    
    libovolna_vira = input("zadej_viru: ")
    celkovy_pocet = 0
    
    
    for radek in reader:
        if radek["vira_txt"] == libovolna_vira.lower():
            celkovy_pocet += 1 
            nazev_mesta = (radek["uzemi_txt"])
            mesto.append(nazev_mesta)
            
    for typ_mesta in mesto:
        item[typ_mesta] = item.get(typ_mesta, 0) + 1 ##zpocitani, jak casto se slovo vyskytuje 
        
    zaver_mesta = max(item, key = item.get)
        
    print ("celkovy pocet: ", celkovy_pocet)
    print ("mesta: ", zaver_mesta)
            
    

