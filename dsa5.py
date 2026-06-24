def does(letters, target):
    for i in range(0, len(letters)) :
        if letters[i]["L"] == target :
            return True , i 
    return False , -1
seen = []

word = input("Enter a word: ")
for letter in word:
    does_it_exists = does(seen, letter)
    if not does_it_exists[0]:
        seen.append({"L": letter, "f":1})
    else:
        seen[does_it_exists[1]]["f"] += 1 
print(seen)