def reverse(world):
    mot_a_lenvers = world[::-1]
    return mot_a_lenvers

def compter_voyelle(texte):
    
    voyelle = "aeiouyAEIOUY"
    nb_voyelle = 0
    nb_consonne = 0
    for caractere in texte :
        if caractere.isalpha() :
            if caractere in voyelle :
                nb_voyelle += 1
            else :
                nb_consonne += 1
    print ("Consonnes: ", nb_consonne , "\nVoyelles: ", nb_voyelle)


while True :
    print ("Quelle operation voullez vous faire ?")
    print ("1. Voir si votre mot est un palindrome")
    print ("2. Voir combien de voyelles et de consonnes votre mot possede")
    print ("3. Exit")
    op= input ("Quelle operation?: ")
    if op == "1":
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
    elif op == "2":
        texte = input ("Votre texte svp: ")
        compter_voyelle(texte)
    elif op == "3":
        break