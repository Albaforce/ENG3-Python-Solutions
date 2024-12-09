a = int(input("How many people need to ride: "))
b = int(input("Ask the user how many people can fit in one taxi: "))
if b != 0 :
  r = a // b 
  if a % b != 0 :
    r = r+1 

  print(f"Number of taxis needed is :{r}")
else :
  print(" The people can't fit in the taxi ")
