first_word = input("Enter your first word: ")
second_word = input("Enter your second word: ")
ca = True
if len(first_word) == len(second_word):
    for i in range (0, len(second_word)):
        if first_word[i] not in second_word :
            print ("Your words aren't anagramme")
            ca = False
            break
        
    if ca:
        print ("Anagram")
else:
    print("uiasdfyuisdahfuiasdfhsdu")
        