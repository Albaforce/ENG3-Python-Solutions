numbers = [1, 2, 3, 4, 5]

while True:
    print("""
    1. Append an element
    2. Insert an element at specific position
    3. Pop an element
    4. Remove an element
    5. Quit
    6. Sort the list
    7. Reverse the list
    8. Search an element
    9. Save the list to a file
    10. Load a list from a file
    """)
    choice = input("Enter your choice: ")
    if choice == '1':
        element = int(input("Enter an element: "))
        numbers.append(element)
        print(numbers)
    elif choice == '2':
        element = int(input("Enter an element: "))
        position = int(input("Enter a position: "))
        numbers.insert(position, element)
        print(numbers)
    elif choice == '3':
        numbers.pop()
        print(numbers)
    elif choice == '4':
        element = int(input("Enter an element: "))
        numbers.remove(element)
        print(numbers)
    elif choice == '5':
        break
    elif choice == '6':
        numbers.sort()
        print(numbers)
    elif choice == '7':
        numbers.reverse()
        print(numbers)
    elif choice == '8':
        element = int(input("Enter an element: "))
        if element in numbers:
            print("Element found")
        else:
            print("Element not found")
    elif choice == '9':
        with open("List.txt", 'w') as file:
            file.write(str(numbers))
    elif choice == '10':
        path = input("enter the path of the file : ")
        file =open(f"{path}", 'r') 
        numbers = file.read()
        print(numbers)
    else:
        print("Invalid choice")
        

