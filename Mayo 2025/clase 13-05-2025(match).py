#uso y explicacion de match 
def suma2(n1,n2):
    print("el resultado de la suma es", n1+n2)
def suma():
    n1=int(input("ingrese un numero"))
    n2=int(input("ingrese otro numero"))
    print("el resultado de la suma es", n1+n2)
def resta():
    n1=int(input("ingrese un numero"))
    n2=int(input("ingrese otro numero"))
    print("el resultado de la resta es", n1-n2)
def multiplicacion():
    n1=int(input("ingrese un numero"))
    n2=int(input("ingrese otro numero"))
    print("el resultado de la multiplicacion es", n1*n2)
def dividir():
    n1=int(input("ingrese un numero"))
    n2=int(input("ingrese otro numero"))
    print("el resultado de la division es", round (n1/n2 , 1))
def calcu():
    while True:
        op=int(input('''seleccione una operacion
                1- suma
                2- resta
                3- multiplicacion
                4- dividir
                5- salir
                '''))

        match op:
            case 1:
                print("suma")
                suma()
            case 2:
                print("resta")
                resta()
            case 3:
                print("multiplicacion")
                multiplicacion()
            case 4:
                print("division")
                dividir()
            case 5: 
                print("salir")
                break
            case _:
                print("opcion invalida")

# suma2(7,9) 

## nuevo menu recursivo
#debe tener 3 programas creado anteriormente
#el menu debe llamar a estos progrmas y ejecutarlos de manera correcta
#debe tener la opcion de salir 
#y la opcion por defecto

def votos():
    num = int(input("Ingrese el número de votos: "))
    Garchomp = 0
    Dragapult = 0

    for i in range(num):
        voto = input("Ingrese su voto (1-Garchomp, 2-Dragapult): ")
        if voto == "1":
            print("Votaste por Garchomp")
            Garchomp += 1
        elif voto == "2":
            print("Votaste por Dragapult")    
            Dragapult += 1
        else:
            print("Voto nulo")

    print("Los votos de Garchomp son:", Garchomp, "y los votos de Dragapult son:", Dragapult)

    if Garchomp > Dragapult:
        print("Ganó Garchomp con", Garchomp, "votos")
    elif Dragapult > Garchomp:
        print("Ganó Dragapult con", Dragapult, "votos")
    elif Dragapult == Garchomp:
        print("Empate de votos")
    else:
        print("Algo falló. ¡Aiuda!")
def carrito():
    Pikachu=0
    Eevee=0
    Gible=0
    Total=0
    Iva=1.19
    while True:
        op=int(input('''selecione una opcion:
                1- elegir productos
                2- Boleta
                3- salir
                '''))
        match op:
            case 1:
                 print("¿Qué pokemon llevara? (Productos sin Iva)")
                 print(" 1-Pikachu $4000")
                 print(" 2-Eevee $4000")
                 print(" 3-Gible $8000")
                 Prod=input()
                 if Prod== "1":
                        print("Has llevado un Pikachu")
                        Pikachu+=1
                        Total+=4000
                 elif Prod== "2":
                        print("Has elegido un Eevee")
                        Eevee+=1
                        Total+=4000
                 elif Prod== "3":
                        print("Has elegido un Gible")
                        Gible+=1
                        Total+=8000
            case 2:
                print("Usted lleva: Pikachu=", Pikachu, "Eevee=", Eevee, "Gible=", Gible)
                print("Por un total de", Total*Iva ,"con Iva incluido") 
            case 3:
                break
def Credito():
    ingresos=int(input("¿De cuanto es su sueldo? "))
    credito=0

    if ingresos>=500000 and ingresos<=1000000:
        credito+=300000
    elif ingresos>=1000001 and ingresos<=1500000:
        credito+=650000
    elif ingresos>=1500001:
        credito+=1000000
    else:
        credito+=0

    educacion=input('''¿cual es su nivel de educacion?
                    1- Basica
                    2- Media
                    3- Superior

                    ''')
    if educacion=="1":
        credito*=1
    elif educacion=="2":
        credito*=1.3
    elif educacion=="3":
        credito*=1.5
    else:
        credito+=0

    nacionalidad=input('''¿Cual es tu nacionalidad?
                       1-Chilena
                       2-Extranjera

                       ''') 

    if nacionalidad=="1":
        credito+=300000
    else:
        credito+=0
    print(f"Despues de evaluar su situacion economica, educacion y nacionalidad su credito disponible es : {credito}")  
def menu_2():
    while True:
        op=int(input('''selecione el programa
                    1- votos
                    2- carrito pokemon
                    3- Credito
                    4- salir'''))
        match op:
            case 1: 
                print("contador de votos")
                votos()
            case 2:
                print("carrito de compras pokemon")
                carrito()
            case 3:
                print("Cantidad de credito disponible")
                Credito()
            case 4:
                break
            case _:
                print("opcion invalida")

menu_2()