x = 5
hak = 5
devam = "e" 


result = 5 < x < 10       # False

# and

# True, True => True
# True, False => False 


result = (x > 5) and  (x <10)  # False 
result = (hak > 0) and (devam=="e")   # True


# or

# True, False => True
# True, True => True
# False, False => False


result = (x > 0) or (x % 2 == 0)    # True
result = (x > 6) or (x % 3 == 0)     # False



# not 

# True => False
# False => True


result = not(x > 0)       # False


# print(result)        


# x, 5-10 arasında olan bir çift sayımı ?


x=int (input("x: "))
result = ((x>5)and(x<10))and(x%2==0)
if result==True:
    print("x 5-10 arasında bir sayı ve çifttir")
else :
    print("x 5-10 arasında bir sayı ve çift değildir")














