# #uso y explicacion de lista
# #      -6 -5 -4 -3 -2  -1 
# lista=[5, 7, 2 , 9, 10, 2]
# #      0  1   2  3   4  5
# print(lista[1]*lista[3])


# for num in lista:
#     print(num)

# hacer una lista de 5 notas 
#luego sacar su promedio 

# notas=[50, 63, 70, 55, 65]
# suma=0
# for nota in notas:
#     print(nota)
#     suma+=nota

# promedio=suma/len(notas)

# print(round (promedio))

# nombres=["Robin", "Noelia", "Coni"]
# apellidos=["Hood", "Maldonado", "chan"]

# for i in range(len(nombres)):
#     print(f"su nombre es {nombres[i]} {apellidos[i]}")

# frutas=["Sandia", "Melon", "Chirimoya"]

# for i  in frutas:
#         print(f"la {i} tiene {len(i)} caracteres")

# autos=["Toyota", "Audi", "Subaru", "Kia", "Mercedes"]

# for auto in autos:
#     print(auto)
#     if "a" in auto.lower():
#         print(f"La marca tiene una a {auto}")
#     else:
#         print("ni una A encontrada")


notas=[50, 63, 70, 25, 65]
suma=0
for nota in notas:
    print(nota)
    suma+=nota
    if nota >=40:
        print("La nota es Azul")
    else:
        print("La nota es Roja")
    

promedio=suma/len(notas)

print(promedio)