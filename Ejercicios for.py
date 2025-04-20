#ejercicios de for
#contar par e impar
num=int(input("ingrese un numero"))
par=0
impar=0

for i in range(num+1):
    
    if i%2==0:
        print("El numero", i," par")
        par=par+1
    else:
        print("El numero", i,  "impar")
        impar+=+1

print("la cantidad de numeros par en la secuencia es:", par)    
print("la cantidad de numeros impar en la secuencia es:", impar) 