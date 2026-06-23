nb_defois = int(input("Combien de nombre? "))
nombre = []
for i in range (1, nb_defois +1):
    num = int(input("Nombre: "))
    nombre.append(num)
nouvelle_liste = []
for num in nombre:
    if num not in nouvelle_liste:
        nouvelle_liste.append(num)
print (nouvelle_liste)