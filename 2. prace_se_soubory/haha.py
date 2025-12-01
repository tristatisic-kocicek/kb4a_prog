import random

cesta = r"C:\Users\nejme\kb4a_prog\2. prace_se_soubory\data\studenti.txt"
cesta_2 = r"C:\Users\nejme\kb4a_prog\2. prace_se_soubory\data\1984.txt"

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




uzivatel = input("nigga what": )
    
with open("aaaaaaaaaaaAAAAAA.txt", "w", encoding="utf-8"):
    file.write(uzivatel)
    












