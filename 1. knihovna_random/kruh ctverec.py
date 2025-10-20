import random
import math

s_ctverec = 1
s_kruh = math.pi / 4
body_ctverec = 0
body_kruh = 0

pocet_bodu = 1000 
for i in range(pocet_bodu):
    x = random.random() 
    y = random.random()
    
    if x**2 + y**2 < 1:
        s_kruh += s_ctverec / pocet_bodu
        body_kruh += 1
    else:
        body_ctverec += 1


body_celkem = body_ctverec + body_kruh

odhad = 4 * body_kruh / body_celkem
print("Odhad hodnoty π je:", odhad)

rozdil = math.fabs - (odhad - math.pi)
print("Rozdíl mezi odhadem a skutečnou hodnotou π je:", rozdil)