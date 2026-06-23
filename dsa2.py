def max_min(num_list):
    plus = max(num_list)
    moins = min(num_list)
    return plus, moins

num_list= []
nombre = int(input ("Combien de fois ?: "))
for i in range (1 , nombre + 1):
    num = int(input("vos nombres: "))
    num_list.append(num)
print (num_list)
print (max_min(num_list))


