# def suma(n1,n2):
#     print(n1+n2)

# def suma_ret():
#     n1=int(input("ingrese un numero :"))
#     n2=int(input("ingrese un numero :"))
#     return n1+n2

# def suma_ret_arg(n1,n2):
#     return n1+n2

# suma(9,8)
# print(suma_ret())
# print(suma_ret_arg(8,9))

'''
realizar una funcion que calcule el iva

realizar otra funcion que al pasarle un precio 
y un numero como percoentaje (ej 20%)
calcule es descuento y muestre el valor final'''

# def iva():
#     iva=int(input("ingrese un valor para calcular el iva"))
#     print(iva*1.19)
# def iva_2(iva):
#     print(iva*1.19)
# def descuento():
#     desc=int(input("Ingres el precio del producto"))
#     print("tiene 20% de descuento")
#     descuento=desc*0.2
#     print(desc-descuento)
# def descuento_2(desc):
#     descuento=desc*0.2
#     return desc-descuento
# iva()
# iva_2(9000)
# descuento()
# n=int(input("ingrese precio del producto"))
# descuento_2(n)

# productos=[
#     {"nombre": "portamina"},
#     {"nombre": "goma"},
# ]

# print(productos[0]["nombre"])

# '''
# 1- agregar articulo
# 2- borrar articulo
# 3-actualizar articulo
# 4- mostrar  listado de articulos
# 5- salir
# '''

def agregar(lista):
    print("Agregue articulo")
    nombre=input("Escriba el articulo a agregar")
    precio=int(input("ingrese precio"))
    lista.append({"nombre": nombre , "precio": precio})
def borrar(lista):
    listaa(lista)
    indice=int(input("Ingrese indice del articulo a borrar"))
    if 0 <= indice < len(articulos):
        del articulos[indice-1]
        print("Articulo borrado")
    else:
        print("indice invalido")
def actualizar(lista):
    listaa(lista)
    actualizar=int(input("ingrese indice de producto a actualizar"))-1
    if 0<= actualizar< len(lista):
        nombre=(input("ingrese nombre"))
        lista[actualizar]["nombre"]=nombre
        print("Nombre actualizado")
        precio=int(input("ingrese precio nuevo"))
        lista[actualizar]["precio"]=precio 
        print("Precio actualizado")
    else:
        print("indice invalido")
def listaa(lista):
    for i, articulo in enumerate(lista):
        print(f"{i+1} - {articulo["nombre"]}  $ {articulo["precio"]}")
def mostrar_menu(lista):
    while True:
        print('''
        1- agregar articulo
        2- borrar articulo
        3-actualizar articulo
        4- mostrar  listado de articulos
        5- salir
        ''')
        op=int(input("Seleecione una opcion (1-6) : "))
        
        match op:
            case 1:
                agregar(lista)
            case 2:
                borrar(lista)
            case 3:
                actualizar(lista)
            case 4:
                listaa(lista)
            case 5:
                print("Saliendo....")
                break
            case _:
                print("Opcion invalida, favor de ingresar opcion de 1 a 6")     
articulos=[]

mostrar_menu(articulos)

personas={
    1:{"nombre": "Liam Neeson",
       "telefono" : 99999999,
       "estadocivil": "soltero",
       "ciudadano": True},
    2:{"nombre": "Cristian Bala",
       "telefono" : 9000456,
       "estadocivil": "soltero",
       "ciudadano": False}
       ,
    3:{"nombre": "Link huan",
       "telefono" : 99999999,
       "estadocivil": "casado",
       "ciudadano": True}
}

print(personas[2]["telefono"])