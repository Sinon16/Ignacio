#calcular el puntaje de credito
#debe de calcular que tanto credito tiene una persona 
# en cierta entidad financiera, debera considerar 
# cantidad de ingresos, nivel educacional y nacionalidad
# cantidad de ingresos
# 500.000 a 1.000.000 :300.000
# 1.000.000 a 1.500.000 : 650.000
# 1.500.001 o mas :1.000.000
# nivel educacional 
# basico: x1 , medio :x1.3 , superior: x1.5
# nacionalidad
# chilena: +300.000, extranjero: +0

# ingresos=int(input("¿De cuanto es su sueldo? "))
# credito=0

# if ingresos>=500000 and ingresos<=1000000:
#     credito+=300000
# elif ingresos>=1000001 and ingresos<=1500000:
#     credito+=650000
# elif ingresos>=1500001:
#     credito+=1000000
# else:
#     credito+=0

# educacion=input('''¿cual es su nivel de educacion?
#                 1- Basica
#                 2- Media
#                 3- Superior

#                 ''')
# if educacion=="1":
#     credito*=1
# elif educacion=="2":
#     credito*=1.3
# elif educacion=="3":
#     credito*=1.5
# else:
#     credito+=0

# nacionalidad=input('''¿Cual es tu nacionalidad?
#                    1-Chilena
#                    2-Extranjera

#                    ''') 

# if nacionalidad=="1":
#     credito+=300000
# else:
#     credito+=0

# print(f"Despues de evaluar su situacion economica, educacion y nacionalidad su credito disponible es : {credito}")    
from random import randint
# num1=int(input("ingrese un numero : "))
# num2=int(input("ingrese un numero mayor al anterior : "))
# if num2>num1:
#         print(f"el {num2} es mayor")
# a=randint(num1,num2)
# print(f"el numero que salio entre ellos fue: {a}")
# print("▄ "*a)
# for i in range(1,a+1):
#         print("▄ ", i)

num1=int(input("ingrese un numero : "))
num2=int(input("ingrese un numero : "))
while num1>num2:
        print("el segundo numero tiene ser mayor")
        num2=int(input("ingrese un numero : "))
a=randint(num1,num2)
print(f"el numero que salio entre ellos fue: {a}")
print("▄ "*a)
for i in range(1,a+1):
        print("▄ ", i)