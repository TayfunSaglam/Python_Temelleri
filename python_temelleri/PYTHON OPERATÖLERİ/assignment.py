x,y,z = 5,16,20

# x,y= y,x         16 5 20    

x += 5    # x= x + 5
x -= 5    # x= x - 5
x *= 5    # x= x * 5
x /= 5    # x= x / 5
x %= 5    # x= x % 5
y //= 5   # y= x// 5
z **= 5   # z= z**5


print(x,y,z)


values= 1,2,3         
print(values)          # (1, 2, 3)
print(type(values))    # <class 'tuple'>


x,y,z = values 
print(x,y,z)          # 1 2 3


values1 = 1,2,3,4,5
a,b,*c = values1
print(a,b,c)        # 1 2 [3, 4, 5]
print(a,b,c[1])     # 1 2 4






