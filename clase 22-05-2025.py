#crear espadas de diamante
#para crear una espada necesitas
#2 diamantes y un palo
#para obtener recursos debe tener 
#el siguiente menu
#1.- minar, se bscan recursos . la posibilidad de encontrar diamantes es 1 entre 7
#y palo 1 entre 3 y la de carbon 1 entre 3
# minar toma 3 segundos
#2.- consultar recursos
#3.- crear espadas
#4.- salir
from random import randint 
import time
diamante=0
palo=0
carbon=0
Espada=0
piedra=0

while True:
    while True:
        try:
            op=int(input('''
                        Seleccione una accion
                        1- Minar
                        2- Consultar Recursos
                        3- crear espadas
                        4- cambio con aldeanos
                        5- volver a casa
                         '''))
            break
        except Exception:
            print("Debe ser un numero entero")
    match op:
        case 1:
            minar=int(input("¿Cuantas veces vas a minar? "))
            for i in range (1, minar+1):
                random=randint(1,21)
                if 1<= random <= 3:
                    diamante+=1
                    print("has obtenido 1 diamante")
                elif 4<= random <=10:
                    palo+=1
                    print("has obtenido 1 palo")
                elif 11<= random <=17:
                    carbon+=1
                    print("has obtenido 1 carbon")
                else:
                    piedra+=1
                    print("has obtenido 1 piedra")
                time.sleep(3)
        case 2:
            print("///Recursos actuales///")
            print(f'''
                   Diamante = {diamante}
                   Palo = {palo}
                   carbon = {carbon}
                   piedra = {piedra}
                   Espadas de diamantes = {Espada}  
                 ''')
        case 3:
            print("creando espada de diamante")
            if diamante>1 and palo>0:
                Espada+=1
                diamante-=2
                palo-=1
                print("se eliminaron 2 diamantes de tus recursos")
                print("se elimina 1 palo de tus recursos")
                print("has creado una espada de diamante con exito")
                print(f"los diamantes que te quedan son {diamante} y de palos {palo}")
            else:
                print("no tienes recursos suficientes")
        case 4:
            if carbon>=10:
                        print("Obtienes 1 diamante")
                        carbon-=10
                        diamante+=1
                        print (f"se elimino 10 de carbon de recursos te quedan: {carbon}")
            else:
                print("no tienes carbon suficiente")  
        case 5:
            print("a casita voy")
            break
        case _:
            print("accion no valida. elige entre 1 a 5")