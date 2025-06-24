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
#             carrito.append(comprar-1)

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
    

# '''
# crear un programa de manejo de notas
# 1- ingresar nota
# 2- borrar nota
# 3- mostrar notas
# 4- sacar promedio , nota mayor y nota menor
# 5- limpiar todas las notas
# 6-salir
# '''
# notas=[]
# suma=0
# while True:
#     while True:
#         try:
#             op=int(input('''
#                     1- ingresar nota
#                     2- borrar nota
#                     3- mostrar notas
#                     4- sacar promedio , nota mayor y nota menor
#                     5- limpiar todas las notas
#                     6-salir
#                     '''))
#             break
#         except Exception:
#             print("Solo debe ingresar numeros enteros entre 1 a 6")

#     match op:
#         case 1:
#             try:
#                 nota =int(input("Ingresa la nota (10-70): "))
#                 if 10 <= nota <= 70:
#                     notas.append(nota)
#                     print("Nota agregada.")
#                     suma+=nota
#                 else:
#                     print("La nota debe estar entre 10 a 70.")
#             except Exception:
#                 print("Solo ingresar numeros enteros")
#         case 2:
#             for i in range(len(notas)):
#                 print(f"nota {i+1} : {notas[i]}")
#             try:
#                 nota =int(input("Ingresa la nota a borrar: "))
#                 if nota in notas:
#                     notas.remove(nota)
#                     print("Nota borrada.")
#                     suma-=nota
#                 else:
#                     print("Esa nota no está en la lista.")
#             except Exception:
#                 print("Solo ingresar numeros enteros")
#         case 3:
#             print("//////Libro de notas//////")
#             print("-----------------------------------")
#             for i in range(len(notas)):
#                 print(f"nota {i+1} : {notas[i]}")
#             print("-----------------------------------")
#         case 4:
#             notas.sort()
#             promedio=suma/len(notas)
#             print(f"El promedio de las notas ingresadas es : {promedio}")
#             print(f"La nota maxima ingresada es : {notas[-1]}")
#             print(f"La nota minima ingresada es : {notas[0]}")
            
#         case 5:
#             notas.clear()
#             print("Todas las notas han sido eliminadas.")
#             suma=0
#         case 6:
#             print("Saliendo del programa.")
#             break
#         case _:
#             print("Opción no válida. Por favor elige entre 1 y 6.")


'''
hacer un sistema de login con diccionario
debe verificar si el usuario existe
de existir le pregunta la contraseña
y da solo 3 oportunidades para acertar 
el diccionario debe de estar previamente 
escrito antes de iniciar el sistema
'''
Logins={
    1:{"usuario": "ignacio", "contraseña": 1234},
    2:{"usuario": "Felipe", "contraseña": 4321},
    3:{"usuario": "Pedro", "contraseña": 5678}
}
intentos=0
while True:
    usuario=input("ingrese su usuario")
    contraseña=int(input("Ingrese su contraseña"))
    if Logins[1]["usuario"]==usuario and Logins[1]["contraseña"]==contraseña:
        print("Bienvenido al sistema")
        break
    elif Logins[2]["usuario"]==usuario and Logins[2]["contraseña"]==contraseña:
        print("Bienvenido al sistema")
        break
    elif Logins[3]["usuario"]==usuario and Logins[3]["contraseña"]==contraseña:
        print("Bienvenido al sistema")
        break
    else:
        print("Datos ingresados invalido")
        intentos+=1
    if intentos==3:
        print("Se ha bloqueado el sistema")
        break