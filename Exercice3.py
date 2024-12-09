total_amount = float(input("Total amount: "))
if total_amount <= 0:
    print("Total amount can't be negative or zero!")
    exit()

Number_Items = int(input("Number of items: "))
if Number_Items <= 0:
    print("Number of items can't be negative or zero!")
    exit()

day = input("Day of the week: ").strip().lower()

weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday"]
weekends = ["saturday", "sunday"]

if day not in weekdays and day not in weekends:
    print("Invalid day!")
    exit()

discount_rate = 0
if day in weekends:
    discount_rate += 0.2
else:
    discount_rate += 0.1

if Number_Items > 5:
    discount_rate += 0.05

total_price = total_amount * (1 - discount_rate)
print(f"Total price after discount: {total_price:.2f} dinars")