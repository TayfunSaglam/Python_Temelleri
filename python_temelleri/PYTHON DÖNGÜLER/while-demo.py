numbers = []

i=0

while i<5:
    sayi=int(input("Sayıyı giriniz:"))
    numbers.append(sayi)
    i+=1

numbers.sort()
print(numbers)    


urunler = []
adet= int(input("Kaç ürün eklemek istiyorsunuz: "))
i=0

while i<adet:
    name=input("Ürün ismi:")
    price=input("Ürün fiyatı:")
    urunler.append({
        "name":name,    
        "price":price
    })
    i+=1

for urun in urunler:
    print(f"ürün adı: {urun['name']}   ürün fiyatı: {urun['price']}")    
