word = input("Enter a word: ")
seen = []
for letter in word:
    if letter not in seen:
        print(letter, ":", word.count(letter))
        seen.append(letter)