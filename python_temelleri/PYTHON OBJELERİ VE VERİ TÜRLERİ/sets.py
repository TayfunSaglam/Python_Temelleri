fruits = {"orange", "apple","banana"}

# print(fruits[0])   indekslenemez

for x in fruits:
    print(x)


fruits.add("cherry")      # "cherry"  ekler
fruits.update(["mango","grape"])  # "mango" ve "grape" ekler
fruits.remove("mango")     # "mango" yu siler
fruits.discard("apple")    # "apple" ı siler
print(fruits)


myList= [1,2,5,4,4,2,1]

print(myList)        # [1, 2, 5, 4, 4, 2, 1]
print(set(myList))   # Tekrarlı elemanlar listeden çıkarılır  {1, 2, 4, 5}








