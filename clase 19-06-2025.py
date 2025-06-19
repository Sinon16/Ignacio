#diccionario dentro de un diccionario

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

# print(personas[2]["telefono"])    


def mostrar_menu(lista):
    def mostrar_lista(lista):
        for i , usuario in lista.items():
            print(f'''{i} - 
                        {usuario["nombre"]}
                        {usuario["telefono"]}
                        {usuario["estadocivil"]}
                        {usuario["ciudadano"]} ''')
    def ingresar(lista):
        nombre=input("ingrese nombre del nuevo usuario : ")
        telefono=int(input("ingrese telefono del nuevo usuario : "))
        estado_civil=int(input("ingrese si el usuario esta 1- Casado 2- soltero : "))
        if estado_civil==1:
            estado="casado"
        elif estado_civil==2:
            estado="soltero"
        else:
            print("Error. Seleccione opcion 1 o 2")
        ciudadano=int(input("ingrese si es ciudadano : 1- Si 2- No : ")) 
        if ciudadano == 1:
            lista[len(lista)+1]={"nombre" : nombre, "telefono" : telefono , "estadocivil" : estado, "ciudadano" : True}
            print("Persona agrega al sistema.")
        elif ciudadano == 2:
            lista[len(lista)+1]={"nombre" : nombre, "telefono" : telefono , "estadocivil" : estado, "ciudadano" : False}
            print("Persona agrega al sistema.")
        else:
            print("Datos invalidos. Vuelva a intentar seleccione opcion 1 o 2 segun corresponda")
    def actualizar(lista):
        mostrar_lista(lista)
        user=int(input("seleccione la persona que va actualizar : "))
        if user in lista:
            while True:
                reemplazar=int(input('''Seleccione que va  actualizar
                                    1- Nombre
                                    2- telefono
                                    3- Estado civil
                                    4- Ciudadano
                                    5- volver al menu anterior
                                    '''))
                match reemplazar:
                    case 1: 
                        nombre=input("ingrese nombre del nuevo usuario")
                        lista[user]["nombre"]=nombre
                    case 2:
                        telefono=int(input("ingrese telefono del nuevo usuario"))
                        lista[user]["telefono"]=telefono
                    case 3:
                        estado_civil=int(input("ingrese si el usuario esta 1- Casado o 2 -soltero"))
                        if estado_civil==1:
                            lista[user]["estadocivil"]="casado"
                        elif estado_civil==2:
                            lista[user]["estadocivil"]="soltero"
                        else:
                            print("Estado civil invalido")
                    case 4:
                        ciudadano=int(input("ingrese si es ciudadano : 1- Si 2- No")) 
                        if ciudadano == 1:
                            lista[user]["ciudadano"]=True
                        elif ciudadano == 2:
                            lista[user]["ciudadano"]=False
                        else:
                            print("Datos invalidos. Vuelva a intentar seleccione opcion 1 o 2 segun corresponda")
                    case 5:
                        break
                    case _:
                        print("opcion invalida")
        else:
            print("Ese usuario no esta registrado.")
    def borrar(lista):
        mostrar_lista(lista)
        borrar=int(input("seleccione persona a borrar"))
        if borrar in lista:
            lista.pop(borrar)
            print(f"La persona {borrar} ha sido eliminada")
        else:
            print("Ese usuario no esta registrado.")

    while True:
        try:
            print('''
            1- Ingresar Persona
            2- Mostrar listado
            3- Actualizar Persona
            4- Borrar Persona
            5- Salir
            ''')
            op=int(input("seleccione una opcion"))
            match op:
                case 1:
                    ingresar(lista)
                case 2:
                    mostrar_lista(lista)
                case 3:
                    actualizar(lista)
                case 4:
                    borrar(lista)
                case 5:
                    print("Saliendo...")
                    break
                case _:
                    print("Opcion invalida.")
        except Exception as e:
            print(f"El error es : {e}")

mostrar_menu(personas)