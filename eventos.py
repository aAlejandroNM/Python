from menu import pedir_opcion
def registrar_eventos(datos):
    datos = dict(datos)
    evento = {}
    evento["nombre"]=input("Ingrese el nombre del evento: ")
    evento["locacion"]=input("Ingrese la locacion: ")
    try:
        evento["dia"] = int(input("Ingrese el dia del evento: "))
    except Exception:
        evento["dia"] = 0

    print("Ingrese 1 si el evento ya se realizo 2 de lo contrario")
    opc = -1
    try:
        opc = int(input("Ingrese la opcion: "))
    except Exception:
        opc = 2
    if opc == 1:
        evento["realizado"] = True
    else:
        evento["realizado"] = False
    
    datos["eventos"].append(evento)
    print("Evento registrado con éxito!")
    return datos

def modificar_evento(datos):
    datos = dict(datos)
    evento = {}
    print("Eventos disponibles: ")

    for i in range(len(datos["eventos"])):
        print(datos["eventos"][i]["nombre"])

    name_soli = input("Cual es el nombre del evento que quiere editar")
    while True:
        for i in range(len(datos["eventos"])):
            if datos["eventos"][i]["nombre"]==name_soli:
                evento["nombre"]=input("Ingrese el nombre del evento: ")
                evento["locacion"]=input("Ingrese la locacion: ")
                try:
                    evento["dia"] = int(input("Ingrese el dia del evento: "))
                except Exception:
                    evento["dia"] = 0
                print("Ingrese 1 si el evento ya se realizo 2 de lo contrario")
                opc = -1
                try:
                    opc = int(input("Ingrese la opcion: "))
                except Exception:
                    opc = 2
                if opc == 1:
                    evento["realizado"] = True
                else:
                    evento["realizado"] = False
                datos["eventos"].append(evento)
                print("Evento registrado con éxito!")
                return datos               
