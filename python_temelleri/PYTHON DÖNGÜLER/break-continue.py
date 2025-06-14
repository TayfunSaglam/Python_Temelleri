name = "Tayfun Sağlam"

for letter in name:
    if letter == "a":
        continue 
    print(letter)


x=0
while x<5:
    x+=1
    if x==2:
        break
    print(x)
    x+=1

x=0
result=0

while x<=100:
    result += x
    x+=1

print("toplam: ",result)