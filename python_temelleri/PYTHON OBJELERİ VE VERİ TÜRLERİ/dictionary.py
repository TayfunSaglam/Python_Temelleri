# key - value 

# 41 => Kocaeli  
# 34 => İstanbul

sehirler= ["kocaeli", "istanbul"]
plakalar= [41,34]

print(plakalar[sehirler.index("kocaeli")])   # 41
print(plakalar[sehirler.index("istanbul")])  # 34



plakalar= { "kocaeli" : 41, "istanbul" : 34}

print(plakalar["kocaeli"])   # 41
print(plakalar["istanbul"])  # 34

 
plakalar["ankara"] = 6
print(plakalar) # {'kocaeli': 41, 'istanbul': 34, 'ankara': 6}



users = {
    "tayfunsağlam": {
          "age": 20,
          "roles": ["admin", "user"],
          "email": "tayfun@gmail.com",
          "address": "istanbul",
          "phone":"0541 212 49 55",
    },
    "sadıkturan": {
          "age": 36,
          "roles": ["user"],
          "email": "sadik@gmail.com",
          "address": "kocaeli",
          "phone":"0541 123 12 34"
          }
}
    
print(users["tayfunsağlam"])  
# {'age': 20, 'roles': ['admin', 'user'], 'email': 'tayfun@gmail.com', 'address': 'istanbul', 'phone': '0541 212 49 55'}
print(users["sadıkturan"]) 
# {'age': 36, 'roles': ['user'], 'email': 'sadik@gmail.com', 'address': 'kocaeli', 'phone': '0541 123 12 34'}

print(users["tayfunsağlam"]["age"])   # 20 
print(users["sadıkturan"]["phone"])   # 0541 123 12 34

print(users["tayfunsağlam"]["roles"][0])  # admin





