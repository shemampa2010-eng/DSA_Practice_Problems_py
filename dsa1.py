def reverse(world):
    mot_a_lenvers = world[::-1]
    return mot_a_lenvers
while True :
    fish = input("Passe un mot pour voir si c'est un palindrome: ")
    mot_a_lenvers = reverse(fish)
    if fish == mot_a_lenvers :
        print ("Lu a l'envers: ", mot_a_lenvers)
        print ("Votre mot est bel et bien un palindrome")
        break
    elif fish == "break":
        break
    else :
        print ("Lu a l'envers: ", mot_a_lenvers)
        print ("Votre mot n'est pas un palindrome. Veuillez reessayer svp")