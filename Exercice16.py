numbers = [1, 2, 3, 4, 5]

i = int(input("Enter index (-1 to quit): "))
while i != -1:
    if not(-1 <= i < len(numbers)):
        print("Index out of range")
        i = int(input("Enter index (-1 to quit): "))
        continue
    v = int(input("Enter new value: "))
    numbers[i] = v
    print(numbers)
    i = int(input("Enter index (-1 to quit): "))