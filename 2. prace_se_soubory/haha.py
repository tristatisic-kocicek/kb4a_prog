import random
import csv
import matplotlib.pyplot as plt


cesta = r"C:\Users\nejme\kb4a_prog\2. prace_se_soubory\data\studenti.txt"
cesta_2 = r"C:\Users\nejme\kb4a_prog\2. prace_se_soubory\data\1984.txt"
cesta_teplota = r""

vybrani_studenti = []

with open (cesta, "r", encoding="utf-8") as file:
    studenti = file.readlines()
    while len (vybrani_studenti) < 5:
        novy_student = random.choice(studenti)
        if novy_student not in vybrani_studenti:
            vybrani_studenti.append(novy_student)
            
vybrani_studenti.sort()

print (vybrani_studenti)

with open("zkouseni_studenti.txt", "w", encoding="utf-8") as file:
    file.write("Selected students:\n")
    for s in vybrani_studenti:
        file.write(s)


uzivatel = input("Enter some text: ")
    
with open("aaaaaaaaaaaAAAAAA.txt", "w", encoding="utf-8") as file:
    file.write(uzivatel)
    
if cesta_teplota:
    try:
        with open(cesta_teplota, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
    
            roky = [] 
            teploty_rano = []
    
            for radek in reader:
                if radek.get("TIME") == "07:00":
                    year = radek.get("YEAR")
                    temp = radek.get("TEMPERATURE")
                    if year and temp:
                        try:
                            teplota = float(temp)
                            teploty_rano.append(teplota)
                            rok = int(year)
                            roky.append(rok)
                        except ValueError:
                            # skip rows with invalid numeric data
                            continue
            
            if teploty_rano:
                prumer = sum(teploty_rano) / len(teploty_rano)
                print(f"Prumer je {round(prumer, 2)} stupnu celsia")
    
                plt.bar(roky, teploty_rano)
                plt.title("Prumer teploty v CR")
                plt.xlabel("Rok")
                plt.ylabel("Teploty ve stupnu celsia")
                plt.show()
            else:
                print("Nebyly nalezeny zadne teploty v 07:00.")
    except FileNotFoundError:
        print(f"Soubor {cesta_teplota!r} nebyl nalezen.")
else:
    print("cesta_teplota neni nastavena; preskakuji zpracovani teplot.")
               
    





  






