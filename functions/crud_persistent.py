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

# Desarrollado por Alexi Durán Gómez : C.C-1.067.031.983