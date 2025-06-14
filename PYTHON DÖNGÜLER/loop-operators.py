#range

for item in range(5,100,10):     #5 den başlar 100e kadar 10'ar artırarak
    print(item)

print(list(range(5,100,10)))    


#enumerate

index = 0
greeting = "Hello There"

for index,letter in enumerate(greeting):

    print(f"index: {index} letter: {letter}")
    

for items in enumerate(greeting):
    print(items)


#zip

list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]
list3 = [100,200,300,400,500]

print(list(zip(list1,list2,list3)))


for item1 in zip(list1,list2,list3):
    print(item1)


for a,b,c in zip(list1,list2,list3):
    print(a)


