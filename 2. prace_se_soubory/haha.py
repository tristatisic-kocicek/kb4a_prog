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
    file.write("nigga what")
    for s in vybrani_studenti:
        file.write(s)




uzivatel = input("nigga what")
    
with open("aaaaaaaaaaaAAAAAA.txt", "w", encoding="utf-8"):
    file.write(uzivatel)
    
with open (cesta_teplota, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    
    roky = [] 
    teploty_rano = []
    
    for radek in reader:
        if radek["TIME"] == "07:00":
            print(radek["YEAR"], radek["TEMPERATURE"])
            teplota = float(radek["TEMPERATURE"])
            teploty_rano.append(teplota)
            rok = int(radek["YEAR"])
            roky.append(rok)
            
    prumer = sum(teploty_rano)  / len(teploty_rano)
    print(f"Prumer je {round(prumer, 2)}stupnu celsia")
    
    plt.bar(roky, teploty_rano)
    plt.title ("Prumer teploty v CR")
    plt.xlabel("Rok")
    plt.ylabel("Teploty ve stupnu celsia")
    plt.show()
               
    





  






