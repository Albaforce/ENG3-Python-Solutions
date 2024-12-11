city =[]
x = input("Enter the city:")
city.append([x , len(x)*1000000])

while x.lower() != 'stop' :
    x = input("Enter the city:")
    city.append([x , len(x)*1000000])

city.pop()
city.sort(key=lambda x: x[1] , reverse=True)
print(city)