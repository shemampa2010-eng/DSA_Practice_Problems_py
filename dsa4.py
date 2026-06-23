number = int(input("Your number pls: "))
is_prime = True
for i in range (2 , round(number/2) +1):
    if number % i == 0 :
        is_prime = False
        break
if is_prime :
    print ("Prime number")
else :
    print ("Your number isn't prime")        
