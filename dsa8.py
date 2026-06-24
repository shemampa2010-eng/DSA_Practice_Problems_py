def second_largest(list_of_num):
    grand = max(list_of_num) 
    list_of_num.remove(grand) 
    return max(list_of_num)
fois = int(input("Combien de nombre voulez vous mettres ?: "))
nombre = []
new = []
for i in range (1, fois +1):
    num = int(input("entrez le nombre: "))
    nombre.append(num)
    if num not in new :
        new.append(num)
print (new)
print(second_largest(new))
