price = float(input("Please type in a price: "))

if price < 0 : 
    print("Invalid price ")
    exit()
    
dinars = int(price)
Centimes = round((price - dinars) * 100)

print("Dinars: " , dinars)
print("Centimes: " , Centimes)