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
        Recibe tres parametros: categoria, descripción y monto
        Retorna True si se crea exitosamente el usuario, o False si no se logra.

    """
    # TODO Parsear a entero el monto
    gasto = {
        "id": create_id(),
        "fecha": str(datetime.now().strftime('%Y-%m-%d')),
        "hora": str(datetime.now().strftime('%H:%M:%S')),
        "categoria": category,
        "descripcion": description,
        "monto": monto
    }
    json_datos = abrirJSON()
    json_datos.append(gasto)

    new_list_costs = guardarJSON(json_datos)
    new_log = logsJSON(gasto)

    if (new_list_costs and new_log):
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
    """
    Esta función fltra por categoria.
    Recibe el nombre de la categoria como argumento de tipo string.
     Retorna una lista de los elementos que pertenecen a esa categoria
    """
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
    """
    Esta función está diseñada para filtrar por año, meses y dias.
    Recibe 3 parametros: 
            por: es un entero entregado como opción por el usuario.
            from: momento desde el que se quiere filtar.
            to: momento hasta el cual se quiere filtrar.
    Retorna una lista con los elementos filtrados.
    """
    rngs = []
    datos = abrirJSON()
    if (por == 1):
        """Filtrar por rango de años"""
        desde = datetime.strptime(_from, '%Y-%m-%d').year
        hasta = datetime.strptime(to, '%Y-%m-%d').year
        
        for i in range(len(datos)):
            anio = datetime.strptime(datos[i]['fecha'], '%Y-%m-%d').year
            if desde <= anio <= hasta:
                rngs.append(datos[i])
        if rngs:
            return rngs  
        else:
            return False

    if (por == 2):
        """Filtrar por rango de mesese"""
        desde = datetime.strptime(_from, '%Y-%m-%d').month
        hasta = datetime.strptime(to, '%Y-%m-%d').month
        for i in range(len(datos)):
            month = datetime.strptime(datos[i]['fecha'], '%Y-%m-%d').month
            if desde <= month <= hasta:
                rngs.append(datos[i])
        if rngs:
            return rngs  
        else:
            return False

    if (por == 2):
        """Filtar por rango de dias"""
        desde = datetime.strptime(_from, '%Y-%m-%d').day
        hasta = datetime.strptime(to, '%Y-%m-%d').day
        for i in range(len(datos)):
            day = datetime.strptime(datos[i]['fecha'], '%Y-%m-%d').month
            if desde <= day <= hasta:
                rngs.append(datos[i])
        if rngs:
            return rngs  
        else:
            return False
    

def total_cost(opt, today):
    """
    Esta función suma el total de los gastos.
    Recibe una opción como parametro.
    Puede retornar la suma de todos los gastos:
        1. Del día.
        2. De la ultima semana.
        3. Del ultimo mes.
    """
    costo = 0
    datos = abrirJSON()

    if (opt == 1):
        """Suma de los gastos del día"""
        for i in range(len(datos)):
            if (int(datetime.strptime(datos[i]['fecha'], '%Y-%m-%d').day) == today):
                costo += int(datos[i]['monto'])

        return costo
    # TODO
    elif (opt == 2):
        """Suma de los gastos del la ultima semana"""
        for i in range(len(datos)):
            fecha = int(datetime.strptime(datos[i]['fecha'], '%Y-%m-%d').day)
            if (fecha <= today-7 and fecha == today):
                costo += int(datos[i]['monto'])

        return costo
    # TODO
    elif (opt == 3):
        """Suma de los gastos del ultimo mes"""
        for i in range(len(datos)):
            if (int(datetime.strptime(datos[i]['fecha'], '%Y-%m-%d').day) <= today-30):
                costo += int(datos[i]['monto'])

        return costo

def cost_report(opts):
    """
    Esta función genera reportes.
    Recice una opción como parametro.
    Retorno:
        1. Genera un reporte con los gastos del día actual.
        2. Genera un reporte con los gastos de la última semana.
        3. Genera un reporte con los gastos del último mes.
    """
    if(opts == 1):
        """Genera un reporte con los gastos del día actual."""
        pass

    if (opts == 2):
        """Genera un reporte con los gastos de la última semana."""

    if (opts == 3):
        """Genera un reporte con los gastos del último mes."""
        pass
  


# Desarrollado por Alexi Durán Gómez : C.C-1.067.031.983