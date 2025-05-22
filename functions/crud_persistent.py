# Proyecto_Python_DuranAlexi
# Funciones DDGG: Es un archivo creado para almacenar las funciones utilizadas en el 
# proceso extracción, carga y guarda de datos en el archivo JSON para persistencia 
import pathlib
ruta = pathlib.Path.cwd()

import json

def abrirJSON():
    """
        Funcion abrir JSON
        No recibe parametros.
        Retorna el contenido del JSON
    """
    dicFinal=[]
    with open("./db/datos.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def guardarJSON(dic):
    with open("./db/datos.json",'w') as outFile:
        json.dump(dic,outFile)
    return True

def cargarLogs():
    dicFinal=[]
    with open("./db/logs.json",'r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal

def logsJSON(dic):
    dicTemporal = []
    #print("Diccionario Importado LOGS")
    
    dicTemporal=cargarLogs()
    #print(dicTemporal)
    dicTemporal.append(dic)
    with open("./db/logs.json",'w') as outFile:
        json.dump(dicTemporal,outFile)

    return True


def abirJSONReport(date, content):
    path = f"./reports/repor_{date}"
    with open(path, 'w') as newReport:
        json.dump(content , newReport)

def guardarJSONReports(reporte_json, name):
    filename = f"./reports/repor_{name}.json"
    # Guardar como archivo JSON
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(reporte_json, f, indent=4, ensure_ascii=False)


# Desarrollado por Alexi Durán Gómez : C.C-1.067.031.983