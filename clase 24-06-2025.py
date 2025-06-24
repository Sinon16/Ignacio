juegos={
    1:{
        "nombre":"Metroid Dread",
        "precio":50000,
        "code":"MMdd2023"
    },
    2:{
        "nombre":"Pikmin 4",
        "precio": 55000,
        "code": "pKMn2022"
    },
}
'''
el nombre debe tener al menos 2 palabras
el precio debe estar entre 8000 y 100000'''
def mostrar_juegos(dic):
    for i,datos in dic.items():
        print(i,datos)
def agregar_juegos(dic):
    largo=list(dic.keys())[-1]
    while True:
        nombre=input("ingrese el nombre del juego : ")
        if validar_nombre(nombre):
            print("Nombre ingresado correctamente")
            break
        else:
            print("El nombre no cumple con los requisitos")
            print("Recuerda que debe constar de 2 palabras al registrar")  
    
    while True:
        precio=int(input("ingrese el precio del juego : "))
        if validar_precio(precio):
            print("El Precio se agrego correctamente")
            break
        else:
            print("El precio ingresado no esta dentro de los parametros")
            print("Recuerda que el rango de precio debe ser entre $8000 y $100000")
    codigo=input("ingrese el codigo del juego : ")
    while True:
        validar_codigo(codigo)
        if validar_codigo(codigo):
            dic[largo+1]={
                "nombre":nombre,
                "precio": precio,
                "code": codigo
            }
            break
        else:
            print("Error , al ingresar el codigo")
            print("Recuerda el codigo debe mantener 2 mayusculas, 2 minusculas y 4 digitos")
            codigo=input("ingrese el codigo del juego : ")
def validar_codigo(code):
    mayuscula=0
    minuscula=0
    digito=0
    for i in code:
        if i.isupper():
            mayuscula+=1
        if i.islower():
            minuscula+=1
        if i.isdigit():
            digito+=1
    if mayuscula==2 and minuscula==2 and digito==4 and len(code)==8:
        return True
    else:
        return False
def actualizar_juegos(dic):
    mostrar_juegos(dic)
    actualizar=int(input("Seleccione cual juego va actualizar : "))
    while True:
        print('''
            1- Nombre
            2- Precio
            3- Codigo
            4- Volver al menu''')
        op=int(input("Seleecione el dato a modificar : "))
        match op:
            case 1:
                while True:
                    nombre=input("ingrese el nombre del juego : ")
                    if validar_nombre(nombre):
                        print("Nombre ingresado correctamente")
                        break
                    else:
                        print("El nombre no cumple con los requisitos")
                        print("Recuerda que debe constar de 2 palabras al registrar")
                dic[actualizar]["nombre"]=nombre
            case 2:
                
                while True:
                    precio=int(input("ingrese el precio del juego : "))
                    if validar_precio(precio):
                        print("El Precio se agrego correctamente")
                        break
                    else:
                        print("El precio ingresado no esta dentro de los parametros")
                        print("Recuerda que el rango de precio debe ser entre $8000 y $100000")
                dic[actualizar]["precio"]=precio
            case 3:
                codigo=input("ingrese el codigo del juego : ")
                while True:
                    validar_codigo(codigo)
                    if validar_codigo(codigo):
                        dic[actualizar]["code"]=codigo
                        break
                    else:
                        print("Error , al ingresar el codigo")
                        print("Recuerda el codigo debe mantener 2 mayusculas, 2 minusculas y 4 digitos")
                        codigo=input("ingrese el codigo del juego : ")
            case 4:
                break
        
            case _:
                print("Error. Opcion no valida")
def borrar_juegos(dic):
    mostrar_juegos(dic)
    borrar=int(input("Seleccione el juego a borrar : "))
    if borrar in dic:
        del dic[borrar]
        print("Se ha borrado el juego")
    else:
        print("EL numero de juego que ingreso no existe.")
def validar_nombre(name):
    nombre_juegos=name.split()
    if len(nombre_juegos)==2:
        return True
        
    else:
        return False
def validar_precio(price):
    if 8000<=price<=100000:
        return True
    else:
        return False      
    
    
while True:
    try:
        print('''
            1- Agregar juego
            2- Mostrar juegos
            3- Actualizar juego
            4- Borrar juego
            5- salir''')
        op=int(input("Selecciona una opcion : "))
        match op :
            case 1:
                agregar_juegos(juegos)
            case 2:
                mostrar_juegos(juegos)
            case 3:
                actualizar_juegos(juegos)
            case 4:
                borrar_juegos(juegos)
            case 5:
                break
            case _:
                print("Error. Opcion no valida")
                
    except Exception as e:
        print("El error es : ", e)
