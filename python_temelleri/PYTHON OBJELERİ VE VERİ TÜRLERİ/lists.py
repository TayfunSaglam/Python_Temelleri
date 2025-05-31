messsage =  "Hello There. My name is Tayfun Sağlam".split()

print(messsage[0])    # Hello


my_list = [1,2,3]
print(my_list)       # [1, 2, 3]

my_list = ["bir",2,True,5.6]
print(my_list)       # ['bir', 2, True]

list1 = ["one","two","there"]
list2 = ["four","five","six"]
numbers = list1 + list2
print(numbers)           # ['one', 'two', 'there', 'four', 'five', 'six']

print(len(numbers))      # 6

userA=["Tayfun", 20]
userB=["Sağlam", 2]

users=userA+userB
users1=[userA, userB]

print(userA)     # ['Tayfun', 20]
print(userB)     # ['Sağlam', 2]
print(users)     # ['Tayfun', 20, 'Sağlam', 2]
print(users1)    # [['Tayfun', 20], ['Sağlam', 2]]

a=users1[1]
print(a[0])           # Sağlam
print(users1[1][0])   # Sağlam





