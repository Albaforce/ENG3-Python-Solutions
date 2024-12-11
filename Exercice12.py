w = int(input("width: "))
if w < 0 :
    print("invalid w")
    exit()

h = int(input("Height: "))
if h < 0 :
    print("invalid h")
    exit()

print((" " + "#" * w) * h)