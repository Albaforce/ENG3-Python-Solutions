user_list = []
x=1
r = input("Have you an existed list (y/n) ?")

if r == 'y' :
    path = input("Please enter the path of the file tha contain the list")
    f = open(f"{path}", 'r')
    user_list = eval(f.read()) # using eval only in trusted file, cause it can execute any code
    f.close()
while x != 0 :
    x = float(input("Enter a number: "))
    user_list.append(x)
    print(f"Current List: {user_list}")    
    user_list_O = user_list
    user_list_O.sort()
    print(f"Sorted List: {user_list_O}")
    user_list_Do = user_list_O
    user_list_Do.reverse()
    print(f"Sorted in reverse List: {user_list_Do}")


r = input("wanna save the list  (y/n)?")

if r == 'y':
    with open("Exo20List.txt", 'w') as file :
        file.write(f"Current List: {user_list} \n")
        file.write(f"Sorted List: {user_list_O} \n")
        file.write(f"Sorted in reverse List: {user_list_Do} \n")

