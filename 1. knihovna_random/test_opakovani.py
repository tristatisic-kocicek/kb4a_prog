import random 

znamky = []

for i in range(10):
    znamky.append(random.randint(1, 5))
    ##pridani do listu 

a = max(znamky)
b = min(znamky)
 
print ((sum(znamky)/10))
print (a, ",", b )

vysledna_znamka = round(sum(znamky)/10)

print (vysledna_znamka)


