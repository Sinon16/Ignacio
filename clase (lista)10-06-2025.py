# nombres=[]
# apellidos=[]
# while True:
#     print('''
#            1-insertar nombre y apellido
#           2- buscar: nombre
#           3- mostrar nombres
#           4- salir
#            ''')
#     op=int(input("selecione una opcion"))
#     match op:
#         case 1:
#             nom=input("ingrese un nombre")
#             nombres.append(nom)
#             ape=input("Ingrese Apellido")
#             apellidos.append(ape)
           
#         case 2:
#             buscar=input("Ingrese nombre a buscar")
#             # buscar2=input("Ingrese apellido a buscar")
                
#             if buscar in nombres:
#                     print(f"Este nombre si se encuentra {buscar}")
#             else:
#                     print("no se encuentra en la lista")

#         case 3:
#             print("///////Nombres en la lista////////")
#             for nombre in range(len (nombres)):
#                 print(f"{nombres[nombre]} {apellidos[nombre]}")
#         case 4:
#             print("saliendo---")
#             break
#         case _:
#             print("opcion invalida")
# productos=["Shingeki no Kyojin" , "Boku no Hero" , "One Piece"]
# precios=[7500 , 8000, 5000]
# carrito=[]
# total=0
# while True:
#     while True:
#         try:
#             op=int(input(''' Seleccione una opcion
#                  1- ingrese productos
#                  2- comprar
#                  3- Boletas
#                  4- Salir
#                  '''))
#             break
#         except Exception:
#             print("debe ingresar solo numeros enteros")
#     match op:
#         case 1:
#             print("Bienvenido a Mangaka")
#             prod=input("ingrese manga a la biblioteca de compra")
#             productos.append(prod)
#             pre=int(input("ingrese precio por volumen del manga"))
#             precios.append(pre)
#         case 2:
#             print("Carrito de compra")
#             print("Productos disponibles")
#             for i in range(len(productos)):
#                 print(f"{i+1}- {productos[i]} $ {precios[i]}")
#             comprar=int(input("selecciona un producto a comprar"))
#             carrito.append((productos[comprar-1],precios[comprar-1]))

#             print(f"Agregando al carrito {productos[comprar-1]} $ {precios[comprar-1]}")
#         case 3:
            
#             print("Boleta de Mangaka")
#             print("///// Resumen de compras//////")
#             for i in range (len (carrito)):
#                 print(f"{i+1}- {productos[i]} $ {precios[i]}")
#                 total+=precios[i]
#             print(f"Su total a pagar neto es {total}")
#             print(f"Su total a pagar con iva es {total*1.19}")
#         case 4:
#             break
    

'''
crear un programa de manejo de notas
1- ingresar nota
2- borrar nota
3- mostrar notas
4- sacar promedio , nota mayor y nota menor
5- limpiar todas las notas
6-salir
'''