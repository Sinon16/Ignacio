# valicaciones de datos

# email=input("Ingrese su email: ")

#verifico si el caracter @ existe en mi variable

# if "@" in email:
#     print("La variable tiene formato mail")
# else:
#     print("La variable NO tiene formato mail")

#validar una clave solo de nuemros enteros
# while True:
#     try:
#         clave=int(input("Ingrese su clave"))
#         break
#     except Exception:
#         print("Error, solo ingrese numeros")

# validar una clave por su largo , por lo menos 5
# clave=input("Ingrese su clave: ")

# verifico que tenga al menos 5 caracteres
# la funcion len() verifica el largo de un objeto
# en este caso la variabble clave    
# if len(clave)>=5:
#     print("La clave tiene el largo correcto")
# else:
#     print("La clave debe tener el menos 5 caracteres")

# ahora verifica que tenga al menos 5 y menor o igual a 12
# if len(clave)>=5 and len(clave)<=12:
#     print("La clave tiene el largo correcto")
# else:
#     print("La clave debe tener el menos 5 caracteres y menos de 12")
  
# verifico si tengo mayusclas y/o minisculas
# y tiene por lo menos un numero

tieneMayus=False
tieneMinus=False
tieneNumero=False

#hacemos un recorrido de cada letra en mi clave
# for letra in clave:
#     # verifico si la letra es mayuscula
#     if letra.isupper():
#         tieneMayus=True
#     # verifico que la letra es minuscula
#     if letra.islower():
#         tieneMinus=True
#     # verifico si tiene por lo meno un numero
#     if letra.isdigit():
#         tieneNumero=True
        
        
# if tieneMayus:
#     print("Tiene por lo menos una mayuscula")
# else:
#     print("NO Tiene por lo menos una mayuscula")
# if tieneMinus:
#     print("Tiene por lo menos una minuscula")
# else:
#     print("NO Tiene por lo menos una miniscula")

# if tieneMayus and tieneMinus and tieneNumero:
#     print("La clave esta ok")
# else:
#     print("Debe intentar nuevamente")

# specials="!#$%&/()=?*{}[]"
# clave="visa#"

# for caracter in clave:
#     if caracter in specials:
#         print("Si es un cracter especial")
  
# clave="Tredf99"      
# def valida_pass(clave):
#     Mayuscula=False
#     Minuscula=False
#     Numero=False
#     for palabra in clave:
#         if palabra.isupper():
#             Mayuscula=True
#         if palabra.islower():
#             Minuscula=True
#         if palabra.isdigit():
#             Numero=True
#     if Mayuscula and Minuscula and Numero and len(clave)==6:
#         print("la clave está bien escrita")
#         return True
#     else:
#         print("la clave está mal escrita")
#         return False
# valida_pass(clave)


# clave=[]

# n=int(input("Ingrese una clave"))
# user=int(input("Ingrese una clave"))
# tipo=int(input("Ingrese una clave"))


# clave.append({"clave": n, "usuario": user, "tipo": tipo})
Vehiculos={}
def validar_patente(clave):
    minu=0
    nume=0
    for i in clave:
        if i.islower():
            minu+=1
        if i.isdigit():
            nume+=1
    if minu==4 and nume==2 and len(clave)==6:
        return True
    else:
        return False

def validar_año(validar):
    nume=0
    for i in validar:
        if i.isdigit():
            nume+=1
    if nume==4 and len(validar)==4:
        return True
    else:
        return False
print("Agregando Vehiculo")
marca=input("Ingrese la marca: ")
año=(input("Ingrese el año : "))

while True:
    validar_año(año)
    if validar_año(año):
        print("Año ingresado correctamente")
        break
    else:
        print("Error al ingresar año")
        print("Solo pueden ser 4 digitos y solo numeros enteros")
        año=(input("Ingrese el año : "))

patente=input("ingrese la patente : ")

while True:
    validar_patente(patente)
    if validar_patente(patente):
        print("La patente se pudo agregar correctamente")
        break
    else:
        print("Error al ingresar patente")
        print("La patente debe tener un largo de 6 con 4 minusculas y 2 digitos")
        patente=input("ingrese la patente : ")
tipo=int(input("ingrese tipo (1-Sedan 2- Camioneta 3- Moto)"))
if not Vehiculos:
    if tipo==1:
        Vehiculos[1]={"marca" : marca , "año": año , "patente": patente , "tipo": "sedan"}
        print("Se ha agregado")
    elif tipo==2:
        Vehiculos[1]={"marca" : marca , "año": año , "patente": patente , "tipo": "camioneta"}
        print("Se ha agregado")
    elif tipo==3:
        Vehiculos[1]={"marca" : marca , "año": año , "patente": patente , "tipo": "moto"}
        print("Se ha agregado")
    else:
        print("Error, opcion invalida")

else:
    num=list(Vehiculos.keys())[-1]
    if tipo==1:
        Vehiculos[num+1]={"marca" : marca , "año": año , "patente": patente , "tipo": "sedan"}
        print("Se ha agregado")
    elif tipo==2:
        Vehiculos[num+1]={"marca" : marca , "año": año , "patente": patente , "tipo": "camioneta"}
        print("Se ha agregado")
    elif tipo==3:
        Vehiculos[num+1]={"marca" : marca , "año": año , "patente": patente , "tipo": "moto"}
        print("Se ha agregado")
    else:
        print("Error, opcion invalida")



