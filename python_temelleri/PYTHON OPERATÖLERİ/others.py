# Identity Operator: is

x = y = [1,2,3]
z = [1,2,3]

print(x==y)    # True
print(x==z)    # True
print(x is y)  # True
print(x is z)  # False 

a= [1,2,3]
b= [2,4]

del a[2]
b[1]= 1
b.reverse()

print(a==b)        # True
print(a is b)      # False
print(a is not b)  # True

# Membership Operator: in


t= ["apple", "banana"]
print("banana" in t)    # True


name= "Tayfun"
print("a" in name)      # True
print("a" not in name)      # False



