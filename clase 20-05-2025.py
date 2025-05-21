# # # #Perros de caza
# # # #Pida al usuario la cantidad de perros
# # # # muestre cual es la cuota minima de conejos
# # # #luego consulte cuantos conejos trajo
# # # #si el perro trajo la cantidad minima
# # # #cumplio la cuota , sino, se queda sin filete
# # # #mostrar resumen de perro que cumplieron y los que no
# import random
# import time

# ## cantidad de perros en caza
# while True:
#         try:
#             cant_perros=int(input("¿Cuantos perros salieron a cazar? "))
#             while cant_perros<1:
#                  print("el valor ingresado debe ser un entero positivo")
#                  cant_perros=int(input("¿Cuantos perros salieron a cazar? "))
#             break
#         except Exception:
#              print("solo debe ingresar numeros enteros")
# ## Variables
# min_conejos=3
# perros=[]
# filete=0
# tabla=0

# ## operacion
# for i in range(1, cant_perros+1):
#     caza_azar=random.randint(1,5)
#     print(f"la cantidad de de conejos que trajo el perro{i+1} es : {caza_azar}")
#     perros.append(caza_azar)
#     if caza_azar>= min_conejos:
#         print("hay filete")
#         filete+=1
#     else:
#         print("hay tabla")
#         tabla+=1
#     time.sleep(1)
# print("///Resumen///")
# # for i  in range(perros, start=1):
# #     print(f"el perro {i} cazo : {perros}")
# for i  in range(1, len (perros)+1):
#     print(f"el perro {i} cazo : {perros[i-1]}")

# print(f"La cantidad de perros que comio filete es : {filete}")
# print(f"La cantidad de perros que toco tabla es : {tabla}")


# #quiere pasar el ramo?
# #pregunte la cantidad de rojos en el curso
# #los talleres hay en el semestre son 4
# #por cada taller asistido obtiene 0.3 decimas
# #si el alumno tiene mas de 1 punto
# #tiene la bendicion del profesor
# #sino, no se le puede ayudar
# # ingrese la nota final y sume las decimas acumuladas
# #muestre si aprueba o reprueba.
# while True:
#     try:
#         cant_rojos=int(input("ingrese la cantidad de alumnos con rojos en el curso"))
#         break
#     except Exception:
#         print("solo debe ingresar numeros enteros")
# decimas_taller=0.3
# asistencia=0
# decimas=0
# nota_sindecimas=0
# nota_total=0

# for i in range(1,cant_rojos+1):
#     print(f"//Alumno{i}//")
#     while True:
#         try:
#             asistencia=int(input("¿ A cuantos talleres asistio ? (0 a 4)"))
#             break
#         except Exception:
#             print("solo debe ingresar numeros enteros")
#     decimas=asistencia*decimas_taller
#     if decimas>1:
#         print("recibe la bendicion del profe")
#     else:
#         print("no hay ayuda")
#     while True:
#         try:
#             nota_sindecimas=float(input("¿cual es su nota final sin decimas?"))
#             break
#         except Exception:
#             print("solo debe ingresar numeros")
#     nota_total=nota_sindecimas+decimas
#     print(f"la nota final del alumno es : {nota_total}")
#     if nota_total>=4.0:
#         print("aprobo")
#     else:
#         print("reprobo")

# try:
#     n1=int(input("ingrese un numero"))
#     n2=int(input("ingrese un numero"))

#     print(f" la division de {n1/n2}")
# except ZeroDivisionError as nombre_de_excepcion:
#     print(f" Se produjo una excepcion: {nombre_de_excepcion}")
# while True:

#     try:
#         op=int(input("ingrese un numero"))
#         break
#     except Exception:
#         print("debe ingresar solo numeros")


#lavado de autos
#crear un menu para lavar autos
#cursar pago del lavado
#ver ventas diarias
#salir
#el lavado teine 3 niveles
#1- full 15000 2-standard 10000  3-basico 7000
#al mostrar las ventas diarias, debe mostrarla
#cantidad de autos que han ingresado y el monto total
#recaudado, tambien debe mostrar el monto mas alto pagado

boleta=0
Full=0
Standard=0
basica=0
print("Lavado de Auto")
while True:
    while True:
        try:
            op=int(input('''
                         selecione una opcion
                        1- cursar pago de lavado
                        2- ver ventas diarias
                        3- salir
                        '''))
            break
        except Exception:
            print("Debe ser un numero entero")
        
    match op:
        case 1:
            while True:
                while True:
                    try:
                        lavado=int(input('''
                                    seleccione un modo de lavado
                                    1- Full $15.000
                                    2- Standard $10.000
                                    3- Basico $7.000
                                    4- Volver al menu anterior
                                    '''))
                        break
                    except Exception:
                        print("Debe ser un numero entero")
                match lavado:
                    case 1:
                        boleta+=15000
                        Full+=1
                    case 2:
                        boleta+=10000
                        Standard+=1
                    case 3:
                        boleta+=7000
                        basica+=1
                    case 4:
                        break
                    case _:
                        print("opcion no validad. Error")
                total=Full+Standard+basica 
        case 2:
            print("///Boleta///")
            print(f"La cantidad de ingresos del dia es : {boleta}")
            print(f"La cantidad de autos lavados actualmente es : {total}")
            if basica>0 and Standard==0 and Full==0:
                print("El producto de mayor valor es el basico por  $ 7000")
            elif Standard>0 and Full==0:
                print("El producto de mayor valor es el standard por  $ 10000")
            else:
                print("El producto de mayor valor es el full por  $ 15000")
        case 3:
            print("Que tenga un buen dia. Adios")
            break
        case _:
            print("opcion no validad. Error intente nuevamente")
