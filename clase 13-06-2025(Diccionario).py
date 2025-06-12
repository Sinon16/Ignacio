# dic={
#     "nombre": "Alan Grant",
#     "numero": 977854521 ,
#     "Casado": True
# }

# print(dic["nombre"])
# dic["nombre"]="Alan Brito"

# print(dic["nombre"])

frutas={
    "Naranja" : 400,
    "Manzana": 500,
    "Pera" : 700,

}
print(frutas)
frutas["Granada"]=1500
print(frutas)

for key, Value in frutas.items():
    print(key,"$", Value)