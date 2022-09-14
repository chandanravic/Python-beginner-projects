import random
abc = random.randrange(10,40)
check = int(input("Enter any number between 10 to 40: "))
while abc!= check:
    if check < abc:
        print("number too low")
        check = int(input("Enter number Greater than previous number: "))
    elif abc > check:
         print ("Number too high")
         check = int(input("Enter number lesser than previous number: "))
    else:
     break 
print("Yeah you read my brain, guessed number right !!11")
