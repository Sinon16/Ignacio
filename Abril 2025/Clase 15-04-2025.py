# Ejercicios de if y while
# sacar promedio de 3 numeros
print("ingrese 3 numeros para sacar el promedio")
n1=float(input("ingrese primera nota "))
n2=float(input("ingrese segunda nota "))
n3=float(input("ingrese tercera nota "))
prom=(n1+n2+n3)/3
print("el promedio es ", prom)

if prom>=4.0:
    print("alumno aprobado")
else: 
    print("alumno reprobado")

# es Mayor de edad o menor de edad
print("ingrese su edad")
edad=int(input())

if edad>=18:
    print("es mayor de edad")
else:
    print("es menor de edad")

# niño menor de 12 años
# adolescente entre 12 y 17 años
# mayor de edad mas o igual a 18 años

print("ingrese su edad")
edad=int(input())

if edad  <12:
    print("niño")
elif edad >=12 and edad <18:
    print("adolescente")
else:
    print("mayor de edad")


# numero mayor

n1=int(input("ingrese un numero "))
n2=int(input("ingrese un numero "))
n3=int(input("ingrese un numero "))

if n1>n2 and n1>n3:
    print("el numero mayor es ", n1)
elif n2>n1 and n2>n3:
    print("el numero mayor es ", n2)
else:
    print("el numero mayor es ", n3)

#clave
while True:
    clave=int(input("ingrese su clave"))
    if clave==1234:
        print("clave correcta")
        break
    else:
        print("clave incorrecta")


 # par o impar

n1=int(input("ingrese un numero"))  

if n1%2==0:
    print("el numero es par")
else:
    print("el numero es impar")
 
   