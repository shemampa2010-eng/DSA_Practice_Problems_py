nm = [0,1]
where= int(input("Jusqu'a quel chiffre voulez vous arriver ?: "))
if where == 0 or where == 1:
    print ("A number over 1 pls")
else:
    for i in range (0, where - 2):
        next = nm[-1] + nm[-2]
        nm.append(next)
print (nm)