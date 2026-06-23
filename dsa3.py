def somme(num_list):
    somme = sum(num_list)
    return somme

num_list= []
nombre = int(input ("Combien de fois ?: "))
for i in range (1 , nombre + 1):
    num = int(input("vos nombres: "))
    num_list.append(num)
print (num_list)
print (sum(num_list))
