word = input("please enter a word: ")

l=len(word)
if l // 2 != 0:
    l += 1
for i in range(30):
    print("*", end="")

print("\n*", end="")

for i in range(14-(l//2)):
    print(" ", end="")

print(word, end="")

for i in range(14-(l//2)):
    print(" ", end="")

print("*")

for i in range(30):
    print("*", end="")
print("\n")

