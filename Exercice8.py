nb = int(input("Enter a number: "))
a=''
if nb % 3 == 0 :
    a = "Fizz"
if nb % 5 == 0 :
    a = a + "Buzz"
print(a)