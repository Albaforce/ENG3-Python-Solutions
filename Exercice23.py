N=-1
while N <= 0 :
    N = int(input("Enter a positive integer N:"))
for i in range(-N,N+1):
    if i == 0:
        continue
    print(i)