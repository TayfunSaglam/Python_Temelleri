list = [1, 2, 3]

tuple = (1, "iki", 33)
 
print(type(list))     # <class 'list'>
print(type(tuple))    # <class 'tuple'>


print(list[2])        # 3
print(tuple[2])       # 33
 

list = ["Ali", "Veli"]
tuple = (" Damla", "Ayşe")


list[0]="Ahmet"
# tuple[0]="Ahmet"

print(list)    # ['Ahmet', 'Veli']
# !!!  print(tuple)    tuple[0]="Ahmet"
# TypeError: 'tuple' object does not support item assignment
# 'tuple' nesnesi öğe atamasını desteklemiyor


tuple= ("damla", " ayşe", "sibel")
names= ("demet", "emel", "yaren") + tuple
print(names)   # ('demet', 'emel', 'yaren', 'damla', ' ayşe', 'sibel')+



