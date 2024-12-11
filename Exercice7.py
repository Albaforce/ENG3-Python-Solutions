year = int(input("Please type in a year: "))

if year <= 0 :
    print("Enter a valid year")
    exit()

if year % 100 == 0 :
    if year % 400 == 0 :
     print("That year is  a leap year.")
     exit()
    print("That year is not a leap year.")
    exit()
elif year % 4 == 0:
    print("That year is  a leap year.")
    exit()

print("That year is not a leap year.")