while True :
    world = input("Un palindrome svp: ")
    mot = world.lower ()
    mot_a_lenvers = mot[::-1]
    if mot == mot_a_lenvers :
       
        print ("Lu a l'envers: ", mot_a_lenvers)
        print ("Votre mot est bel et bien un palindrome")
        break
    elif mot == "break":
        break
    else :
        print ("Lu a l'envers: ", mot_a_lenvers)
        print ("Votre mot n'est pas un palindrome. Veuillez reessayer svp")