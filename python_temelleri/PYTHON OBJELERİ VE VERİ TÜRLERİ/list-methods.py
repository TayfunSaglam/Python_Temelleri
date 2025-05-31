numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ["a", "g", "s", "b", "y", "a", "s"]

val = min(numbers) #1

val = max(numbers)  # 16
     
val = min(letters)  # a

val = max(letters)  # y

val = numbers[3:6]  # [16, 4, 9]   

val = numbers[:3]   # [1, 10, 5]

val= numbers[4:]    # [4, 9, 10]

numbers[4] = 40     # [1, 10, 5, 16, 40, 9, 10]

numbers.append(49)  # 49 rakamını ekler
numbers.append(59)  # [1, 10, 5, 16, 40, 9, 10, 49, 59]
  

numbers.insert(3, 7)   # 3.indeksten hemen önce 7 rakamını ekler
# [1, 10, 5, 7, 16, 40, 9, 10, 49, 59]
 
numbers.pop()          # [1, 10, 5, 7, 16, 40, 9, 10, 49]
numbers.pop(0)         # [10, 5, 7, 16, 40, 9, 10, 49]
numbers.pop(-1)        # [10, 5, 7, 16, 40, 9, 10]

numbers.remove(10)     # 10 sayısını bulur ve siler    [5, 7, 16, 40, 9, 10]
numbers.remove(10)     # [5, 7, 16, 40, 9]

numbers=[1, 10, 5, 78, 16, 40, 9, 10, 49, 52]

numbers.sort()  # sayısal olarak sıralanır
# [1, 5, 9, 10, 10, 16, 40, 49, 52, 78]

letters.sort()  # alfabetik olarak sıralanır
# ['a', 'a', 'b', 'g', 's', 's', 'y']

numbers.reverse()  # listeyi tam tersi döndürür
# [78, 52, 49, 40, 16, 10, 10, 9, 5, 1]

letters.reverse() 
# ['y', 's', 's', 'g', 'b', 'a', 'a']

print(numbers.count(10)) # 10 sayısından ne kadar var söyler  ==> 2
print(letters.count("a")) # a harfinden kaç tane var söyler  ==> 2

numbers.clear()   # tüm elemanları temizler 
letters.clear()   # []

print(letters)
print(numbers)         









