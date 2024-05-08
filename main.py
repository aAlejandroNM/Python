#Una empresa está organizando la agenda de eventos para el mes de agosto. Por lo tanto requiere un programa que:
# Permita registrar a los participantes de los eventos de agosto pidiendo: documento, nombre, edad y cargo.
# Permita registrar los eventos  pidiendo: nombre del evento, locación y día del mes
# Permita quitar del registro a los participantes .
# Permita eliminar y/o modificar eventos.
# Para participar los empleados deben cancelar un aporte de 50.000 COP. Por lo tanto el programa también debe:
# Saber cuantos empleados no han cancelado aún el aporte y cuanto dinero suma la deuda.
# Saber cuales empleados (listarlos) no han cancelado.
# No permitir quitar del registro a participantes que ya hayan pagado, pues no se aceptan devoluciones
# Marcar eventos ya realizados.
# No permitir eliminar o modificar eventos ya realizados.
# Aspectos a tener en cuenta: 
# La estructura a utilizar es libre, solo se pide que sea ordenada y coherente. 
# Todo debe ser dentro de un menú que se repite para no perder la información y al presionar la opción de salida se debe pedir confirmación de la misma. 
# Se deben manejar la excepciones

#imports
from datos import *
from menu import *
from participantes import *
from eventos import *

#Constants
RUTA_BASE_DE_DATOS = "eventos.json"

datos = cargar_datos(RUTA_BASE_DE_DATOS)

while True:
    menu_principal()
    opc = pedir_opcion()
    if opc == 1:
        datos = registrar_participante(datos)
    elif opc == 2:
        datos = eliminar_participante(datos)
    elif opc == 3:
        datos = pagar_participante(datos)
    elif opc == 4:
        datos == registrar_eventos(datos)
    elif opc == 5:
        print("opcion 5")
    elif opc == 6:
        print("opcion 6")
    elif opc == 7:
        cuales_participantes_sin_pagar(datos)
    elif opc == 8:
        cuantos_participantes_sin_pagar(datos)
    elif opc == 9:
        print("opcion 9")
    elif opc == 10:
        participantes_del_mes(datos)
    elif opc == 11:
        print("Salió!!")
        break

guardar_datos(datos, RUTA_BASE_DE_DATOS)