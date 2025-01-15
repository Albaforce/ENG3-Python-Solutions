
def length(lst):
    return len(lst) # use the pre-built function len
        
def mean(lst):
    s = 0      # s is where we store the sum
    for i in lst:
        s = s + i  # sum every element in the list 
    return s/length(lst)

def range_of_list(lst):
    lst.sort() # sort the list so that i can retrieve the max and the min easily [ first and last element]
    return lst[length(lst)-1]-lst[0]

liste = []

while True :
    try:
        x = input("Add a number to the list \"if you wanna stop enter 'stop'\": ")
        if x.lower() == "stop":
            break
        x = float(x)
        liste.append(x)
        
    except ValueError:
        print("You must enter a number sir !") # if the user enter an caractere or string, this message will be displayed
        
    
print(f"the length of the list is {length(liste)}")  
print(f"The mean = {mean(liste)}")    
print(f"The range of the list is :{range_of_list(liste)}")

