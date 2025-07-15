
#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, procesador, video]}
productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i5', 'Nvidia GTX1050'],
'2175HD': ['Lenovo', 14, '4GB', 'SSD', '512GB', 'Intel Core i5', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i7', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i3', 'integrada'],
'GF75HD': ['Asus', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'123FHD': ['Lenovo', 14, '6GB', 'DD', '1T', 'AMD Ryzen 5', 'integrada'],
'342FHD': ['Lenovo', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 7', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 3', 'Nvidia GTX1050'],
}
#stock = {modelo: [precio, stock]}
stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 
# 'FS1230HD': [249990,0] no esta en productos este modelo,
}
marcas=[]
modelos=[]
def mostrar_producto(x):
    for i in x:
        print(f"Marca: {x[i][0]} - Pantalla: {x[i][1]} - RAM: {x[i][2]} - Disco: {x[i][3]} - GB de DD: {x[i][4]} - Procesador: {x[i][5]} - Tarjeta de video: {x[i][6]}")

def stock_marca(marca):
    mostrar_producto(marca)
    consultar=input("Ingrese marca a consultar: ").upper()
    suma=0
    for i in marca:
        revisar=marca[i][0].upper()
        cantidad=stock[i][1]
        if consultar==revisar:
            suma+=cantidad
    print(f"El stock es: {suma}")
    
def busqueda_precio(p_min_max):
    try:
        precio_minimo=int(input("Ingrese precio minimo: "))
        precio_maximo=int(input("Ingrese precio maximo: "))
    except Exception:
        print("Solo debe ingresar numeros enteros.")
    for i in p_min_max:
        precio=p_min_max[i][0]
        limite=p_min_max[i][1]
        if precio_minimo <= precio <= precio_maximo:
            if limite!=0:
                marca=productos[i][0]
                marcas.append(marca)
                modelo=i
                modelos.append(modelo)

    if len(marcas)==0:
        print("No hay notebooks en ese rango de precios")
    else:
        print("Los notebooks entre los precios  consultados son: ")
        for i in range(len(marcas)):
            print(f"Marca: {marcas[i]} - Modelo: {modelos[i]}")

def actualizar_precio(model):
    contador_si=0
    for i in model:
        print(f"Modelo: {i} - Precio: {model[i][0]}")
    while True:
        modelo=input("Ingrese modelo a actualizar: ")
        if modelo in model:
            nuevo=input("Ingrese precio nuevo:")
            model[modelo][0]=nuevo
            print("Precio Actualizado!!")
        else:
            print("El modelo no existe.")
        repetir=input("Desea actualizar otro precio (si/no)?: ").lower()
        if repetir=="si":
            contador_si+=1
        elif repetir=="no":
            break
        else: 
            print("Debe ingresar solamente si o no")
            print("volviendo al menu principal")
            break

while True:
    try:
        print('''
            ***MENU Principal***
            1. Stock Marca
            2. Búsqueda por precio
            3. Actualizar Precio
            4. Salir''')
        op=int(input("Selecione una opcion: "))

        match op:
            case 1:
                stock_marca(productos)
            case 2:
                busqueda_precio(stock)
            case 3:
                actualizar_precio(stock)
            case 4:
                print("Programa finalizado")
                break
            case _:
                print("Debe seleccionar una opcion valida!!")

    except Exception as e:
        print(f"El error es : {e}")
