# # crear un menu de carrito con las siguientes opciones 
# # 1.- Ingresar nombre del usuario
# # Sera mostrado en la boleta con un saludo
# #2.- comprar, poner productos para poder comprar
# #con su precio correspondiente
# #3.- sacar boleta, calcular el precio neto y el precio mas IVA. Mostrar totales
# #4.- salir
# #condieraciones:
# #por lo menos 3 producots
# #No hay limites de compra
# #se puede salir en cualquier momento 
# #los montos de los producots son fijos

# usuario=input("ingrese nombre : ")
# precio=0
# producto=0
# while True:
#     op=int(input(''' Seleccione una opcion
#                  1- Comprar producto
#                  2- Boletas
#                  3- Salir
#                  '''))
#     match op:
#         case 1:
#             print("Productos")
            
#             while True:
                
#                 producto=int(input('''Seleccione un producto
#                             1- manga de shingeki $ 7500
#                             2- manga de Black clover $ 9000
#                             3- manga de Jujutsu kaisen $8500
#                             4- manga de boku no hero $ 7000
#                             5- Salir
#                             '''))
#                 if producto == 1:
#                     print(f"lleva manga de shingeki")
#                     precio+=7500
#                 elif producto ==2:
#                     print(f"lleva manga de Black clover")
#                     precio+=9000
#                 elif producto ==3:
#                     print(f"lleva manga de Jujutsu kaisen")
#                     precio+=8500
#                 elif producto ==4:
#                     print(f"lleva manga de Boku no hero")
#                     precio+=7000
#                 elif producto ==5:
#                     break
#                 else:
#                     print("opcion invalida, no selecciono ningun producto")

#         case 2:
#             print (f"Saludo {usuario} tu boleta actual es:")
#             print(f"lleva un total neto de ${precio}")
#             print (f"El total con IVA es: {precio*1.19}")
#         case 3:
#             print(f"Vuelva nuevamente {usuario}")
#             print(f"El total de sus productos es: {precio*1.19}")
#             break
#         case _:
#             print("opcion invalida")


cant_alumno=int(input("ingrese la cantidad de alumnos : "))
nota=0
promedios=[]
total_promedio=0
for i in range(1, cant_alumno+1):
    print(f"alumno {i}")
    suma=0
    cant_notas=int(input("ingrese cantidad de notas : "))
    for n in range(cant_notas):
        nota=float(input(f"ingresa la nota {n+1}"))
        suma+=nota
    promedio=suma/cant_notas
    total_promedio+=promedio
    promedios.append(promedio)
    print(f"el alumno {i} tiene un promedio de: {promedio}")
    if promedio>= 4.0:
        print(f"el alumno {i} aprobo")
    else:
        print(f"el alumno {i} reprobo")
print("/resumen de promedios")
for i, prome2 in enumerate(promedios, start=1):
    print(f" Alumno {i} : Promedio = {prome2}")
curso=total_promedio/cant_alumno

print(f"El promedio del curso es : {curso}")
    
