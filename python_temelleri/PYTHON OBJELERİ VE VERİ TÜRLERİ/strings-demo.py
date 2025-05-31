message = "Hello There. My name is Tayfun Sağlam"

message = message.upper()

print(message.upper())       # HELLO THERE. MY NAME IS TAYFUN SAĞLAM
print(message.lower())       # hello there. my name is tayfun sağlam
print(message.title())       # Hello There. My Name Is Tayfun Sağlam
print(message.capitalize())  # Hello there. my name is tayfun sağlam



print(message.split())      # ['Hello', 'There.', 'My', 'name', 'is', 'Tayfun', 'Sağlam']
print(message.split("."))   # ['Hello There', ' My name is Tayfun Sağlam']
print(message.split(" "))   # ['Hello', 'There.', 'My', 'name', 'is', 'Tayfun', 'Sağlam']


# message = message.split()   # Önce parçalarına ayrıldı.Ardından parçaların arasına yıldız işareti kondu
print('*'.join(message))    # Hello*There.*My*name*is*Tayfun*Sağlam


print(message.find("Tayfun"))  # 24.indeksten itibaren olduğunu belirtir

print(message.startswith("H"))  #True   H ile başlıyor
print(message.startswith("k"))  #False  k ile değil m ile bitiyor


print(message.replace("Tayfun","Ahmet"))  # Cümledeki Tayfun yerine Ahmet yazar  ==>   Hello There. My name is Ahmet Sağlam


print(message.center(50))


