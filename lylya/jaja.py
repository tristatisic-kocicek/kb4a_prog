a = int (input())
delitele = []

if a!=0:
    for i in range(1, a):
        if a%i != 0:
            delitele.append(i)
else: 
    print("nahh zadej znovu: ", int(input()))
            
print (delitele)