# # Conoceremos la estructura y uso de for

# for i in range (5):
#     print("repeticion numero ", i+1)

#ingrese un numero e imprima la tabla de ese num

# num=int(input("ingresa el numero"))
# for i in range (1,13):
#     print("la tabla de ", num , " es:")
#     print(i, "x" , num , " = ",i*num)


#ingresa un numero e imprime toda la tabla hasta ese numero

# num=int(input("ingresa el numero"))
# for i in range (num+1):
#     for p in range (1,13):
#         print("la tabla de " ,i ,"es")
#         print(i*p)

# #secuencia hacia atras

# for i in range(10,0,-1):
#     print(i)

# #pida un nombre al usuario y saludelo 3 veces 

# nombre=input("ingrese un nombre")
# for i in range(3):
#     print("hola", nombre)


# #pida al usuario 3 notas y saque el promedio
# #uso de for obligatorio


# suma=0
# for i in range(3):
#     n1=float(input("ingrese nota ") )
#     suma=suma+n1


# promedio=suma/3  
# print("el promedio del alumno es ", round(promedio))

# #pida al usuario ingrese las notas y saque el promedio
# #uso de for obligatorio

# notas=int(input("ingrese la cantidad de notas nota ") )
# suma=0
# for i in range(notas):
#     n1=int(input("ingrese nota ") )
#     suma=suma+n1


# promedio=suma/notas
# print("el promedio del alumno es ", round(promedio))

#ingrese la cantidad de numeros

n=int(input("ingrese la cantidad de numeros ") )
suma=0
for i in range(n):
    n1=int(input("ingrese el numero a sumar"))
    suma=suma+n1

print("la suma de tus numeros es :", suma)  

