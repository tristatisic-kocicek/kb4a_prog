import random 

spravna_odpoved = 0

for i in range (3): 

    a = random.randint (0, 10)
    b = random.randint (0, 10)

    znak = input("vyber si znak: ")

    print (a, znak, b, " = ?")
    
    odpoved = int(input("zadej odpoved: "))
    
    
    if znak == "-":
        if odpoved == (a - b):
            spravna_odpoved += 1
        

            
    elif znak == "+": 
        if odpoved == (a + b):
            spravna_odpoved += 1
            
print ("spravne: ", spravna_odpoved, "/ 0")
            
