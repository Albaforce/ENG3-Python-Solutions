P1 = int(input("Please type in the age of the first person: "))
if P1 <= 0:
        print("Error! Enter a valid age")
        exit()
P2 = int(input("Please type in the age of the second person: "))
if P2 <= 0:
        print("Error! Enter a valid age")
        exit()
if P1 > P2 :
    print(f"The older age is: {P1}")
elif P2 > P1:
    print(f"The older age is: {P2}")
else :
    print("Both people are the same age!")