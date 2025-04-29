# def es_primo(numero):
#     if numero < 2:
#         return False
#     for i in range(2, int(numero ** 0.5) + 1):
#         if numero % i == 0:
#             return False
#     return True

# # Solicitar al usuario un número
# numero = int(input("Ingresa un número: "))

# # Verificar si es primo
# if es_primo(numero):
#     print(f"{numero} es un número primo.")
# else:
#     print(f"{numero} no es un número primo.")
# a=int(input())
# for i in range (1,10001):
#     print(f"{i}x{a} = {i*a}")

# edad=-1
# while edad<0 or edad>100:
#     edad=int(input())
#     if edad <0 or edad>100:
#         print("error, fuera de rango")
# print("ingresado exitosamente")
# print(edad)       

# #pida al usuario un numero y clasifiquelo como par o impar
# #muestre los pares e impares de el uno hasta ese numero

# n1=int(input("ingrese un numero"))  
# for i in range (1,n1+1):
#     if i%2==0:
#         print(f"el numero es {i} par")   
#     else:
#         print(f"el numero es {i} impar")

# #pida al usuario ingresar numero, al fina debe mostrar cuantos numero
# #se ingresaron y mostrar la suma de todos ellos, para terminar, debe poner
# #la palabra salir

# num=int(input("ingrese un numero"))
# print("0=Salir")
# suma=0

# while num!=0:
#     suma+=num
#     cont+=1
#     print(f"el numero ingresado es {num}")
#     print(f"la suma del factorial que lleva es: {suma}")
#     num=int(input("ingrese numero para ir sumando"))

# print(f"la cantidad de numeros ingresados son {cont}")
# print(f"la suma del factorial que lleva es: {suma}")
    


# # print(f"termino el proceso y quedo con la suma de: {suma}") 

# # #pida al usuario ingresar un numero y multiplicalo por un numero al 
# # #azar entre 2 y 8.si
# # #el numero es mayor que 50, logro la meta , sino , intente nuevamente
# import random
# while True:
#         num=int(input("ingrese un numero"))
#         multiplicador=random.randint(2,8)
#         Resultado=num*multiplicador
#         print(f"tu numero es:{num} tu multiplicador es:{multiplicador} y dio como resultado{Resultado}")
#         if Resultado>50:
#               print("has logrado la meta")
#               break
#         else:
#               print("has fallado, intente nuevamente")


# #ingrese un numero positivo, multiplicarlo por 5, restarle 8,
# #sumarle 3 y dividirlo por 2

num=int(input("ingrese un numero positivo"))
multiplicacion=num*5
resta=multiplicacion-8
suma=resta+3
division=suma/2
print(f"tu numero {num} se multiplico por 5 se le resto 8 se le sumo 3 y termino divido por 2 dio como resultado {division} ")

#adividar el numero
#genere un numero aleatorio entre 1 y 50
#pida al usuario ingresar un numero
#si el numero ingresado es mayor muestre "El numero a adivinar es mayor
# de forma contrarioa escriba "El numero a adivinar es menor"
#hacer 2 versiones , una de intentos infinitos y otra con solo 5