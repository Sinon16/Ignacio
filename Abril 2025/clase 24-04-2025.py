# # contar vocales y consonantes de una palabra
  
# palabra=input("Ingrese una palabra")
# contador_Vocales=0
# consonante=0
# espacio=0
# for i in palabra:
#     if i.lower() in"aeiou":
#         contador_Vocales+=1
#     elif i in " ":
#         espacio+=1

#     else:
#         consonante+=1
#     print(i)

# print(f"Esta palabra tiene {contador_Vocales} vocales y {consonante} consonantes")

# frase=input("Ingrese una frase")
# contador_Vocales=0
# consonante=0
# caracter=0
# espacio=0
# for i in frase:
#     caracter+=1
#     if i.lower() in"aeiou":
#         contador_Vocales+=1
#     elif i==" ":
#         espacio+=1    
#     else:
#         consonante+=1
#     print(i)

# print(f"Esta frase contiene {caracter} caracteres y tiene {contador_Vocales} vocales con {consonante} consonantes")

# #explicacion y uso de while
# num=0

# while num>5:
#     print("hola")
#     num+=1
# import time
# num=10
# while num>0:
#     print(num)
#     time.sleep(1)
#     num-=1

# clave=3344
# intento=0
# intento_max=3

# while intento < intento_max:
#     password=int(input("ingrese su clave: "))
#     if password==clave:
#         print("clave correcta")
#         break
#     else:
#         print(" clave incorrecta")
#         intento+=1
#         print(f" le quedan {intento_max-intento}")

# if intento==intento_max:
#     print("Demasiado intentos, sistema bloqueado")
# else:
#     print("Ingreso al sistema")


#pedir al usuario numeros que se vayan sumando
#y mostrar al final la suma de todos.
#salir del programa al poner un cero

# num=int(input("ingrese un numero"))
# suma=0

# while num!=0:
#     suma+=num
#     print(f"la suma del factorial que lleva es: {suma}")
#     num=int(input("ingrese numero para ir sumando"))
    

# print(f"termino el proceso y quedo con la suma de: {suma}") 

# #Supermercado pokemon
# Pikachu=0
# Eevee=0
# Gible=0
# Total=0
# Iva=1.19
# print("¿Qué pokemon llevara? (Productos sin Iva)")
# print(" 1-Pikachu $4000")
# print(" 2-Eevee $4000")
# print(" 3-Gible $8000")
# print(" 0-para terminar la compra")
# Prod=input()

# while Prod!=0:
 
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
#     elif Prod=="0":
#         break
#     else:
#         print("Pokemon elegido invalido.")

#     Prod=input()


# print("Usted lleva: Pikachu=", Pikachu, "Eevee=", Eevee, "Gible=", Gible)
# print("Por un total de", Total) 
# print("Por un total de", Total*Iva ,"con Iva") 

    
 



