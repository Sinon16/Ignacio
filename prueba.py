autos = {
    'ABC123': ['Toyota', 2020, 'Gasolina', '1.6L'],
    'DEF456': ['Chevrolet', 2019, 'Diesel', '2.0L'],
    'GHI789': ['Hyundai', 2021, 'Eléctrico', '0.0L'],
    'JKL321': ['Mazda', 2022, 'Gasolina', '2.5L'],
    "AAA333": ["kia", 2025, "Diesel", "2.5L"]
}
modelo="AAA333"
marca="kia"
año=2025
combustible= "Diesel"
cilindraje="2.5L"

autos[modelo]=[marca,año,combustible,cilindraje]
stock = {
    'ABC123': [14, 12500000],
    'DEF456': [0, 10400000],
    'GHI789': [4, 17900000],
    'JKL321': [6, 15500000],
    'ZZZ000': [2, 8900000] , # Este auto no existe en Autos
    "AAA333": [5, 17900000]
}
cantidad=5
precio=17900000
stock[modelo]:[cantidad, precio]
def mostrar_stock(x):
    for i in x:
        print(f"{i} : Stock : {x[i][0]} , Precio: {x[i][1]}")

def mostrar_autos(x):
    for i in x:
        print(f"Modelo: {i} - Marca: {x[i][0]} - Año: {x[i][1]} - Combustible: {x[i][2]} - Cilindraje: {x[i][3]}")
         
def validar_cilindraje(x):
    digito=0
    punto=0
    L=0
    for i in x:
        if i.isdigit():
            digito+=1
        if "." in i:
            punto+=1
        if "L" in i:
            L+=1
    if digito==2 and punto==1 and L==1 and len(x)==4:
       return True
    else:
        return False
        
def precio_alto(x):
    precio_alto=-1
    for i in x:
        precio=x[i][1]
        if precio > precio_alto:
            precio_alto=precio
            modelo=i
    print(f"El modelo mas caro es {modelo} con un valor de ${precio_alto}")  
'''
dado los diccionarios anteriores cerar un programa con sl sigueinte menu
1.- Mostrar stock de cada uno 
2.- Buscar precio mas alto 
3.- Actualizar stock 
4.- Borrar un modelo ( considerar borarr el stock tb)
5.- Actualizar datos vehiculo
6.- Salir
'''

while True:
    try:
        print('''
              Menu Principal
            0.- Mostrar datos de vehiculos
            1.- Mostrar stock de cada uno 
            2.- Buscar precio mas alto 
            3.- Actualizar stock 
            4.- Borrar un modelo ( considerar borarr el stock tb)
            5.- Actualizar datos vehiculo
            6.- Salir''')
        op=int(input("Selecione una opcion: "))
        match op:
            case 0:
                mostrar_autos(autos) 
            case 1:
                mostrar_stock(stock)
            case 2:
                precio_alto(stock)  
            case 3:
                mostrar_stock(stock) 
                modelo=input("ingrese modelo: ").upper()
                if modelo in stock:
                     nuevo=int(input("ingrese nuevo stock: "))
                     stock[modelo][0]=nuevo
                     print("Stock Actualizado.")
                else:
                    print("No existe modelo")
            case 4:
                mostrar_autos(autos)
                modelo=input("ingrese modelo: ").upper()
                if modelo in autos:
                    del autos[modelo]
                if modelo in stock:
                    del stock[modelo]
                print("El modelo ha sido borrado si existia.")
            case 5:
                mostrar_autos(autos)
                modelo=input("ingrese modelo: ").upper()
                if modelo in autos:
                    while True:
                        print('''
                            1- Marca
                            2- Año
                            3- Tipo de Combustible
                            4- Cilintraje
                            5- volver al menu principal''')
                        op=int(input("selecione una opcion: "))
                        match op:
                            case 1:
                                marca=input("Ingrese Marca: ")
                                autos[modelo][0]=marca
                                print("Marca actualizada")
                            case 2:
                                año=input("ingrese Año: ")
                                autos[modelo][1]=año
                                print("Año actualizado")
                            case 3:
                                combustible=int(input("ingrese tipo de combustible: 1- Gasolina 2- Diesel 3- Electrico ") )
                                if combustible==1:
                                    autos[modelo][2]="Gasolina"
                                    print("Tipo de combustible Actualizado")
                                elif combustible==2:
                                    autos[modelo][2]="Diesel"
                                    print("Tipo de combustible Actualizado")
                                elif combustible==3:
                                    autos[modelo][2]="Electrico"
                                    print("Tipo de combustible Actualizado")
                                else:
                                    print("Error.")
                            case 4:
                                while True:
                                    cilindraje=input("ingrese Cilindraje: ").upper()
                                    if validar_cilindraje(cilindraje):
                                        autos[modelo][3]=x
                                        print("Cilindraje Actualizado")
                                        break
                                    else:
                                        print("Recuerde el cilindraje se ingresa con digito punto digito y finaliza con L")
                                        print("Ejemplo: 1.5L")

                            case 5:
                                break
                            case _:
                                print("opcion no valida")
            case 6:
                break
            case _:
                print("opcion no valida")

    except Exception as error:
        print(f"El error es : {error}")