# #ejercicios de for
# #contar par e impar
# num=int(input("ingrese un numero"))
# par=0
# impar=0

# for i in range(num+1):
    
#     if i%2==0:
#         print("El numero", i," par")
#         par=par+1
#     else:
#         print("El numero", i,  "impar")
#         impar+=+1

# print("la cantidad de numeros par en la secuencia es:", par)    
# print("la cantidad de numeros impar en la secuencia es:", impar) 

# # Contador de Votos
# num = int(input("Ingrese el número de votos: "))
# Garchomp = 0
# Dragapult = 0

# for i in range(num):
#     voto = input("Ingrese su voto (1-Garchomp, 2-Dragapult): ")
#     if voto == "1":
#         print("Votaste por Garchomp")
#         Garchomp += 1
#     elif voto == "2":
#         print("Votaste por Dragapult")    
#         Dragapult += 1
#     else:
#         print("Voto nulo")

# print("Los votos de Garchomp son:", Garchomp, "y los votos de Dragapult son:", Dragapult)

# if Garchomp > Dragapult:
#     print("Ganó Garchomp con", Garchomp, "votos")
# elif Dragapult > Garchomp:
#     print("Ganó Dragapult con", Dragapult, "votos")
# elif Dragapult == Garchomp:
#     print("Empate de votos")
# else:
#     print("Algo falló. ¡Aiuda!")


# # Auto liviano o pesado
# num = int(input("Ingrese un número de vehículos: "))

# total = 0 


# for i in range(1, num + 1):
#     auto = int(input("¿Auto liviano (1) o pesado (2)?: "))
    
#     if auto == 1:
#         print("Vehículo liviano, costo $3000")
#         total += 3000
#     elif auto == 2:
#         print("Vehículo pesado, costo $5000")
#         total += 5000
#     else:
#         print("Error: tipo de vehículo no válido. No se suma al total.")

# print("Las ganancias diarias son $", total)
