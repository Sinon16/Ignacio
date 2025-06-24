#diccionario dentro de un diccionario

# personas={
#     1:{"nombre": "Liam Neeson",
#        "telefono" : 99999999,
#        "estadocivil": "soltero",
#        "ciudadano": True},
#     2:{"nombre": "Cristian Bala",
#        "telefono" : 9000456,
#        "estadocivil": "soltero",
#        "ciudadano": False}
#        ,
#     3:{"nombre": "Link huan",
#        "telefono" : 99999999,
#        "estadocivil": "casado",
#        "ciudadano": True}
# }



# def mostrar_menu(lista):
#     def mostrar_lista(lista):
#         for i , usuario in lista.items():
#             print(f'''{i} - 
#                         {usuario["nombre"]}
#                         {usuario["telefono"]}
#                         {usuario["estadocivil"]}
#                         {usuario["ciudadano"]} ''')
#     def ingresar(lista):
#         largo=list(lista.keys())[-1]
#         nombre=input("ingrese nombre del nuevo usuario : ")
#         telefono=int(input("ingrese telefono del nuevo usuario : "))
#         estado_civil=int(input("ingrese si el usuario esta 1- Casado 2- soltero : "))
#         if estado_civil==1:
#             estado="casado"
#         elif estado_civil==2:
#             estado="soltero"
#         else:
#             print("Error. Seleccione opcion 1 o 2")
#         ciudadano=int(input("ingrese si es ciudadano : 1- Si 2- No : ")) 
#         if ciudadano == 1:
#             lista[largo+1]={"nombre" : nombre, "telefono" : telefono , "estadocivil" : estado, "ciudadano" : True}
#             print("Persona agrega al sistema.")
#         elif ciudadano == 2:
#             lista[largo+1]={"nombre" : nombre, "telefono" : telefono , "estadocivil" : estado, "ciudadano" : False}
#             print("Persona agrega al sistema.")
#         else:
#             print("Datos invalidos. Vuelva a intentar seleccione opcion 1 o 2 segun corresponda")
#     def actualizar(lista):
#         mostrar_lista(lista)
#         user=int(input("seleccione la persona que va actualizar : "))
#         if user in lista:
#             while True:
#                 reemplazar=int(input('''Seleccione que va  actualizar
#                                     1- Nombre
#                                     2- telefono
#                                     3- Estado civil
#                                     4- Ciudadano
#                                     5- volver al menu anterior
#                                     '''))
#                 match reemplazar:
#                     case 1: 
#                         nombre=input("ingrese nombre del nuevo usuario")
#                         lista[user]["nombre"]=nombre
#                     case 2:
#                         telefono=int(input("ingrese telefono del nuevo usuario"))
#                         lista[user]["telefono"]=telefono
#                     case 3:
#                         estado_civil=int(input("ingrese si el usuario esta 1- Casado o 2 -soltero"))
#                         if estado_civil==1:
#                             lista[user]["estadocivil"]="casado"
#                         elif estado_civil==2:
#                             lista[user]["estadocivil"]="soltero"
#                         else:
#                             print("Estado civil invalido")
#                     case 4:
#                         ciudadano=int(input("ingrese si es ciudadano : 1- Si 2- No")) 
#                         if ciudadano == 1:
#                             lista[user]["ciudadano"]=True
#                         elif ciudadano == 2:
#                             lista[user]["ciudadano"]=False
#                         else:
#                             print("Datos invalidos. Vuelva a intentar seleccione opcion 1 o 2 segun corresponda")
#                     case 5:
#                         break
#                     case _:
#                         print("opcion invalida")
#         else:
#             print("Ese usuario no esta registrado.")
#     def borrar(lista):
#         mostrar_lista(lista)
#         borrar=int(input("seleccione persona a borrar"))
#         if borrar in lista:
#             lista.pop(borrar)
#             print(f"La persona {borrar} ha sido eliminada")
#         else:
#             print("Ese usuario no esta registrado.")

#     while True:
#         try:
#             print('''
#             1- Ingresar Persona
#             2- Mostrar listado
#             3- Actualizar Persona
#             4- Borrar Persona
#             5- Salir
#             ''')
#             op=int(input("seleccione una opcion"))
#             match op:
#                 case 1:
#                     ingresar(lista)
#                 case 2:
#                     mostrar_lista(lista)
#                 case 3:
#                     actualizar(lista)
#                 case 4:
#                     borrar(lista)
#                 case 5:
#                     print("Saliendo...")
#                     break
#                 case _:
#                     print("Opcion invalida.")
#         except Exception as e:
#             print(f"El error es : {e}")

# mostrar_menu(personas)


'''
crear gestion de vehiculos
crear programa para un parking de autos
se debe ingresar
marca, año, patente , tipo
marca: tipo string, se debe tipear la marca
año: tipo int, solo debe tener 4 digitos
patente: debe tener 4 letras minusculas y 2 digitos
tipo: S= sedan, C=camioneta, M=moto

se debe validar cada aspecto y tener un mantenedor para
todos los vehiculos motorizados

1- ingresar vehiculo
2- mostrar vehiculos
3- actualizar vehiculo
4- borrar vehiculo
5- mostrar estadisticas: ultimo vehiculo ingresado y total en garage
6- salir
 '''
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
        año=int(año)
        return True
    else:
        return False


while True:
    try:
        print('''
            1- ingresar vehiculo
            2- mostrar vehiculos
            3- actualizar vehiculo
            4- borrar vehiculo
            5- mostrar estadisticas: ultimo vehiculo ingresado y total en garage
            6- salir
            ''')
        op=int(input("Seleccione una opcion"))
        match op:
            case 1:
                print("Agregando Vehiculo")
                marca=input("Ingrese la marca: ")
                año=(input("Ingrese el año : "))
                validar_año(año)
                if validar_año(año):
                     print("Año ingresado correctamente")
                else:
                    print("Error al ingresar año")
                    print("Solo pueden ser 4 digitos y solo numeros enteros")

                patente=input("ingrese la patente : ")
                validar_patente(patente)
                if validar_patente(patente):
                    print("La patente se pudo agregar correctamente")
                else:
                    print("Error al ingresar patente")
                    print("La patente debe tener un largo de 6 con 4 minusculas y 2 digitos")
                tipo=int(input("ingrese tipo (1-Sedan 2- Camioneta 3- Moto)"))
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
            case 2:
                for i , vehiculo in Vehiculos.items():
                    print(f"{i+1} - {vehiculo["marca"]} {vehiculo["año"]} {vehiculo["patente"]} {vehiculo["tipo"]} ")
            case 3:
                for i , vehiculo in Vehiculos.items():
                    print(f"{i+1} - {vehiculo["marca"]} {vehiculo["año"]} {vehiculo["patente"]} {vehiculo["tipo"]} ")
                    actualizar=int(input("Ingrese vehiculo que va actualizar : "))
                    while True:
                        print('''
                            1- Marca
                            2- Año
                            3- Patente
                            4- Tipo
                            5- volver al menu anterior''')
                        seleccion=int(input("seleccione que dato va a modificar"))
                        match seleccion:
                            case 1:
                                marca=input("Ingrese la marca: ")
                                Vehiculos[actualizar]["marca"]=marca
                                print("Se ha modificado el dato")
                            case 2:
                                año=int(input("Ingrese el año : "))
                                Vehiculos[actualizar]["año"] =año
                                print("Se ha modificado el dato")
                            case 3:
                                patente=input("ingrese la patente : ")
                                Vehiculos[actualizar]["patente"]=patente
                                print("Se ha modificado el dato")
                            case 4:
                                tipo=int(input("ingrese tipo (1-Sedan 2- Camioneta 3- Moto)"))
                                if tipo==1:
                                    Vehiculos[actualizar]["tipo"]="sedan"
                                    print("Se ha modificado el dato")
                                elif tipo==2:
                                    Vehiculos[actualizar]["tipo"]="camioneta"
                                    print("Se ha modificado el dato")
                                elif tipo==3:
                                    Vehiculos[actualizar]["tipo"]="moto"
                                    print("Se ha modificado el dato")
                                else:
                                    print("Error, opcion invalida")
                            case 5:
                                break
                            case _:
                                print("Error. Opcion invalida")
                                print("Recuerda seleccionar opcion de 1 a 5")
            case 4:
                for i , vehiculo in Vehiculos.items():
                    print(f"{i+1} - {vehiculo["marca"]} {vehiculo["año"]} {vehiculo["patente"]} {vehiculo["tipo"]} ")
                borrar=int(input("ingresa vehiculo a borrar : "))
                if borrar in Vehiculos:
                    del Vehiculos[borrar]
                    print("Se ha borrado el vehiculo")
                else:
                    print("Vehiculo no existe en la lista")
            case 5:
                cant=list(Vehiculos.keys())
                ultimo=list(Vehiculos.keys())[-1]
                print(f"La cantidad de vehiculos en el garage es : {cant}")
                print(f'''El ultimo vehiculo agregado es : 
                       {Vehiculos[ultimo]["Marca"]}
                       {Vehiculos[ultimo]["año"]}
                       {Vehiculos[ultimo]["patente"]}
                       {Vehiculos[ultimo]["tipo"]}''')
            case 6:
                print("Saliendo....")
                break
            case _:
                print("Error. Opcion invalida")
                print("Recuerda seleccionar opcion de 1 a 6")
    except Exception as e:
        print(f"El error es : {e}")