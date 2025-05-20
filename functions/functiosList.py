# Proyecto_Python_DuranAlexi
# Controller file: El archivo controler o controlador es un archivo creado para aislar la logica de funcionamiento del programa 
# con el objetivo de modularizarlo y que de está manera sea mucho más legible al igual que facil de modificar.
from datetime import datetime
from db.test_data import test_db
from functions.crud_persistent import *
from functions.auxfunctions import *

def add_new_cost(category, description, monto):
    """
        Esta función se encarga de aislar la logica de creación de un nuevo gasto, llamando las funciones para guardar en la base de datos
    """
    gasto = {
        "fecha": recort_date(str(datetime.now())),
        "categoria": category,
        "descripcion": description,
        "monto": monto
    }
    json_datos = abrirJSON()
    json_datos.append(gasto)

    new_list_costs = guardarJSON(json_datos)

    if (new_list_costs):
        return True
    
    else:
        return False


def list_costs():
    """
        Esta función se encarga de enviar la lista de todos los costos.
        No recibe parametros.
        Retorna una lista de costos que hay en la base de satos, en caso no haber, retorna falso.
    """
    if (abrirJSON):
        return abrirJSON()
    else:
        return False
    
def filter_by_category(category):
    categorys = []
    datos = abrirJSON()
    for i in range(len(datos)):
        if (category == datos[i]['categoria']):
            categorys.append(datos[i])
    if categorys:
        return categorys
    else:
        return False

# TODO
def filter_by_range_date(por, _from, to,):
    rngs = []
    datos = abrirJSON()
    if (por == 1):
        desde = recort_date_year(_from)
        hasta = recort_date_year(to)
        for i in range(len(datos)):
            print(datos[i]['fecha'])
            print(recort_date_year(datos[i]['fecha']))

            # if (range(desde, hasta) == recort_date_year(datos[i]['fecha'])  and (recort_date_year(datos[i]['fecha']) is not None)):
                # if (range(desde, hasta) == recort_date_year(datos[i]['fecha'])):
                    # print(datos[i])
        # if rngs:
            # return rngs  
        # else:
            # return False

    if (por == 2):
        desde = recort_date_mont(_from)
        hasta = recort_date_mont(to)
        for i in range(len(datos)):
            if (range(desde, hasta) == recort_date_mont(datos[i]['fecha'])):
                print(datos[i])
        if rngs:
            return rngs  
        else:
            return False

    if (por == 2):
        desde = recort_date_day(_from)
        hasta = recort_date_day(to)
        for i in range(len(datos)):
            if (range(desde, hasta) == recort_date_day(datos[i]['fecha'])):
                print(datos[i])
        if rngs:
            return rngs  
        else:
            return False
    

def total_cost():
    """
    Esta función
    """
    gastos = abrirJSON()
    for i in range(len(gastos)):
        print(gastos['monto'])

def cost_report():
    """
    Esta función
    """
    pass
  


# Desarrollado por Alexi Durán Gómez : C.C-1.067.031.983