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
    #evento = {}
    print("Eventos disponibles: ")

    for i in range(len(datos["eventos"])):
        print(datos["eventos"][i]["nombre"])

    name_soli = input("Cual es el nombre del evento que quiere editar")
    while True:
        for i in range(len(datos["eventos"])):
            if datos["eventos"][i]["nombre"]==name_soli:
                datos["eventos"][i]["nombre"]=input("Ingrese el nombre del evento: ")
                
                datos["eventos"][i]["locacion"]=input("Ingrese la locacion: ")
                try:
                    datos["eventos"][i]["dia"] = int(input("Ingrese el dia del evento: "))
                except Exception:
                    datos["eventos"][i]["dia"] = 0
                print("Ingrese 1 si el evento ya se realizo 2 de lo contrario")
                opc = -1
                try:
                    opc = int(input("Ingrese la opcion: "))
                except Exception:
                    opc = 2
                if opc == 1:
                    datos["eventos"][i]["realizado"] = True
                else:
                    datos["eventos"][i]["realizado"] = False

                print("Evento modificado con éxito!")
                return datos               
def finalizar_evento(datos):
    datos = dict(datos)

    decision = input("desea eliminar un evento? si/no")
    if decision == "si":
        eliminar_evento(datos)


    print('Los eventos sin finalizar son: ')

    for i in range(len(datos["eventos"])):
        if datos["eventos"][i]["realizado"] == False:
            print(datos["eventos"][i]["nombre"])

        
    
    cambio = input("Cual es el evento que quiere finalizar")
    for i in range(len(datos["eventos"])):
        if datos["eventos"][i]["nombre"]==cambio:
            print("Ingrese 1 para marcar como finalizado")
            opc = -1
            try:
                opc = int(input("Ingrese la opcion (1) para marcar como finalizado: "))
            except Exception:
                opc = 2
            if opc == 1:
                datos["eventos"][i]["realizado"] = True
            else:
                datos["eventos"][i]["realizado"] = False

            print("Evento modificado con éxito!")
            return datos               

def eventos_mes(datos):
    datos = dict(datos)

    for i in range(len(datos["eventos"])):
        print("Nombre: ",datos["eventos"][i]["nombre"], end=",")
        print("Locacion: ",datos["eventos"][i]["locacion"], end=",")
        print("Dia: ",datos["eventos"][i]["dia"], end=",")
        print("Finalizado: ",datos["eventos"][i]["realizado"])

def eliminar_evento(datos):
    datos = dict(datos)
    print('eventos disponibles: ')
    for i in range(len(datos["eventos"])):
        print(datos["eventos"][i]["nombre"])
    evento_solicitado = input("Cual es el evento que desea eliminar")
    for i in range(len(datos["eventos"])):
        if datos["eventos"][i]["nombre"] == evento_solicitado:
            datos["eventos"].pop(i)
            print("Evento eliminado!")
            return datos
        else:
            print("Participante no existe")
            return datos
        