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

vehiculos={
    
    
}
def validar_año(x):
    numero=0
    for i in x:
        if i.isdigit():
            numero+=1
    if numero==4 and len(x)==4:
        return True
    else:
        return False

def validar_patente(x):
    numero=0
    minusculas=0
    for i in x:
        if i.islower():
            minusculas+=1
        if i.isdigit():
            numero+=1
    if minusculas==4 and numero==2 and len(x)==6:
        return True
    else:
        return False

def mostrar_lista(x):
    for i,vehiculo in x.items():
        print(f"{i} - Marca: {vehiculo["marca"]}, Año: {vehiculo["año"]}, Patente : {vehiculo["patente"]}, Tipo de vehiculo : {vehiculo["tipo"]}")

def agregar_vehiculos(x):
    marca=input("ingrese marca de vehiculo : ")
    while True:
        año=input("ingrese año de vehiculo : ")
        if validar_año(año):
            print("Se ha agregado año correctamente")
            break
        else:
            print("Error. Recuerda deben ser solo 4 digitos")
    while True:
        patente=input("ingrese patente de vehiculo : ")
        if validar_patente(patente):
            print("Se ha agregado patente correctamente.")
            break
        else:
            print("Error. Recuerda deben ser solo 2 digitos y 4 minusculas")
    tipo=int(input("ingrese tipo de vehiculo (1-sedan ,2- camioneta,3- moto): "))
    if len(x)==0:
        if tipo ==1:
            x[1]={"marca":marca,"año":año,"patente":patente,"tipo":"sedan"}
        elif tipo==2:
            x[1]={"marca":marca,"año":año,"patente":patente,"tipo":"camioneta"}
        elif tipo==3:
            x[1]={"marca":marca,"año":año,"patente":patente,"tipo":"moto"}
        else:
            print("opcion no valida")
    else:
        ultimo=list(x.keys())[-1]
        if tipo ==1:
            x[ultimo+1]={"marca":marca,"año":año,"patente":patente,"tipo":"sedan"}
        elif tipo==2:
            x[ultimo+1]={"marca":marca,"año":año,"patente":patente,"tipo":"camioneta"}
        elif tipo==3:
            x[ultimo+1]={"marca":marca,"año":año,"patente":patente,"tipo":"moto"}
        else:
            print("opcion no valida")

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
        op=int(input("Selecione una opcion : "))
        
        match op:
            case 1:
                agregar_vehiculos(vehiculos)
            case 2:
                mostrar_lista(vehiculos)
            case 3:
                mostrar_lista(vehiculos)
                actualizar=int(input("Seleccione vehiculo para actualizar datos"))
                if actualizar in vehiculos:
                    while True:
                        print('''
                            1- Marca
                            2- Año
                            3- Patente
                            4- tipo de vehiculo
                            5- Volver al menu principal''')
                        dato=int(input("Seleccione el dato a modificar"))
                        match dato:
                            case 1:
                                marca=input("ingrese marca de vehiculo : ")
                                vehiculos[actualizar]["marca"]=marca
                            case 2:
                                while True:
                                    año=input("ingrese año de vehiculo : ")
                                    if validar_año(año):
                                        print("Se ha agregado año correctamente")
                                        break
                                    else:
                                        print("Error. Recuerda deben ser solo 4 digitos")
                                vehiculos[actualizar]["año"]=año
                            case 3:
                                while True:
                                    patente=input("ingrese patente de vehiculo : ")
                                    if validar_patente(patente):
                                        print("Se ha agregado patente correctamente.")
                                        break
                                    else:
                                        print("Error. Recuerda deben ser solo 2 digitos y 4 minusculas")
                                vehiculos[actualizar]["patente"]=patente
                            case 4:
                                tipo=int(input("ingrese tipo de vehiculo (1-sedan ,2- camioneta,3- moto): "))
                                
                                if tipo ==1:
                                    vehiculos[actualizar]["tipo"]="sedan"
                                elif tipo==2:
                                    vehiculos[actualizar]["tipo"]="camioneta"
                                elif tipo==3:
                                    vehiculos[actualizar]["tipo"]="moto"
                                else:
                                    print("opcion no valida")
                            case 5:
                                break
                            case _:
                                print("Error. Opcion invalida")
                else:
                    print("Vehiculo no existente")


            case 4:
                mostrar_lista(vehiculos)
                borrar=int(input("Seleccione el vehiculo a borrar : "))
                if borrar in vehiculos:
                    del vehiculos[borrar]
                    print("Se ha borrado el vehiculo")
                else:
                    print("Vehiculo no existente")
            case 5:
                garage=list(vehiculos.keys())
                ultimo=list(vehiculos.keys())[-1]
                print(f'''El ultimo vehiculo agregado es : 
                      Marca: {vehiculos[ultimo]["marca"]}
                      Año :  {vehiculos[ultimo]["año"]}
                      Patente : {vehiculos[ultimo]["patente"]}
                      Tipo de Vehiculo : {vehiculos[ultimo]["tipo"]}''')
                print(f"La cantidad de vehiculos en el garage es : {len(garage)}")
            case 6:
                break
            case _:
                print("Error. Opcion invalida")
        
    except Exception as e:
        print("El error es : ",e)