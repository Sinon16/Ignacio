# # preguntar la cantidad de productos
# #  mostrar un listado a seleccionar cada producto con su precio 
# # dar precio con iva

# Cant=int(input("¿Cuantos productos llevara?"))
# Pikachu=0
# Eevee=0
# Gible=0
# Total=0
# Iva=1.19

# for i in range(Cant):
#     Prod=input(("¿Qué producto llevara? 1-Pikachu $4000 2-Eevee $4000 3-Gible $8000 (Productos sin Iva)"))
#     if Prod== "1":
#         print("Has llevado un Pikachu")
#         Pikachu+=1
#         Total+=4000
#     elif Prod== "2":
#         print("Has elegido un Eevee")
#         Eevee+=1
#         Total+=4000
#     elif Prod== "3":
#         print("Has elegido un Gible")
#         Gible+=1
#         Total+=8000
#     else:
#         print("Pokemon elegido invalido.")


# print("Usted lleva: Pikachu=", Pikachu, "Eevee=", Eevee, "Gible=", Gible)
# print("Por un total de", Total*Iva ,"con Iva incluido")      

# palabra=input("Ingrese una palabra")
# contador_Vocales=0
# consonante=0
# for i in palabra:
#     if i=="a":
#         contador_Vocales+=1
#     elif i=="e":
#         contador_Vocales+=1
#     elif i=="i":
#         contador_Vocales+=1
#     elif i=="o":
#         contador_Vocales+=1
#     elif i=="u":
#         contador_Vocales+=1
#     else:
#         consonante+=1
#     print(i)

# print("esta palabra tiene", contador_Vocales, "Vocales y",consonante, "consonantes.")
  
# palabra=input("Ingrese una palabra")
# contador_Vocales=0
# consonante=0
# for i in palabra:
#     if i.lower() in"aeiou":
#         contador_Vocales+=1
#     else:
#         consonante+=1
#     print(i)

# print("esta palabra tiene", contador_Vocales, "Vocales y",consonante, "consonantes.")


# list=[]
# num=int(input("ingresa numero de pokemones que te gustan"))

# for i in range(num):
#     Pokemon=input("que pokemones te gustan ?")
#     list.append(Pokemon)


# print("Lista de Pokémon:")
# for i, Pokemon in enumerate(list, start=1):
#     print(f"{i}. {Pokemon}")

# #formas de concadenar

# nombre=input("ingrese su nombre")
# edad=input("ingrese su edad")

# print("hola", nombre, "su edad es", edad)
# print(f"hola{nombre} su edad es {edad} ")

# #pida al usuario una frase y cuente los caracteres
# nombre=input("ingrese una frase")
# contador=0
# for i in nombre:
#     print(i)
#     contador+=1
# print(f"la frase tiene {contador} caracteres")

#len= cuenta la cantiad de elementos dentro de la variable

# nombre=input("ingrese una frase")
# cont=len(nombre)

# print(f"la frase tiene {cont} caracteres")

# #contar los votos y mostrar los resultados
# #Definir que es el ganador4

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


# #Supermercado pokemon
# Cant=int(input("¿Cuantos Pokemones llevara?"))
# Pikachu=0
# Eevee=0
# Gible=0
# Total=0
# Iva=1.19

# for i in range(Cant):
#     print("¿Qué pokemon llevara? (Productos sin Iva)")
#     print(" 1-Pikachu $4000")
#     print(" 2-Eevee $4000")
#     print(" 3-Gible $8000")
#     Prod=input()
#     if Prod== "1":
#         print("Has llevado un Pikachu")
#         Pikachu+=1
#         Total+=4000
#     elif Prod== "2":
#         print("Has elegido un Eevee")
#         Eevee+=1
#         Total+=4000
#     elif Prod== "3":
#         print("Has elegido un Gible")
#         Gible+=1
#         Total+=8000
#     else:
#         print("Pokemon elegido invalido.")


# print("Usted lleva: Pikachu=", Pikachu, "Eevee=", Eevee, "Gible=", Gible)
# print("Por un total de", Total*Iva ,"con Iva incluido") 