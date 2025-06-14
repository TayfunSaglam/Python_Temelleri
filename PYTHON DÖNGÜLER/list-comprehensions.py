numbers=[]

for x in range(10):
    numbers.append(x)
print(numbers)

numbers1 = [x for x in range(10)]
print(numbers1)

numbers = [x*x for x in range(10) if x%3==0]
print(numbers)
 

myString="Hello"
myList=[]

for letter in myString:
    myList.append(letter)
print(myList)


myList= [letter for letter in myString]
print(myList)


result=[ x if x%2==0 else "Tek" for x in range(1,10)]
print(result)


result1=[]
for x in range(3):
    for y in range(3):
        result1.append((x,y))

print(result1)

