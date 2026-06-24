fois = int(input("Combien de nombre voulez vous mettres ?: "))
nombre = []
new = []
for i in range (1, fois +1):
    num = int(input("entrez le nombre: "))
    nombre.append(num)
    if num not in new :
        new.append(num)
print (nombre)
print (new)  
