# Funciones Auxiliares: En este archivo se guardan funciones de auxiliares, diseñadas para ayudar a 
# la mudularización del proyecto, con el objetivo de contribuir a la facilidad 
# para leer e interpretar el código.
from db import test_data

# Recortar fechas en por los espacios en blanco
def recort_date_year(date: str):
    """
        Está función se encarga de recortar fechas en formato string.
        Recibe la fecha como parametro.
        retorna el primer indice de una lista obtenida al aplicar el metodo de string .split() con el valor en tipo entero
    """
    list = date.split('-')
    print(int(list[0]))

# Recortar fechas en por los espacios en blanco
def recort_date_mont(date: str):
    """
        Está función se encarga de recortar fechas en formato string.
        Recibe la fecha como parametro.
        retorna el primer indice de una lista obtenida al aplicar el metodo de string .split() con el valor en tipo entero
    """
    list = date.split('-')
    print(int(list[1]))

def recort_date_day(date):
    """
        Está función se encarga de recortar fechas en formato string.
        Recibe la fecha como parametro.
        retorna el primer indice de una lista obtenida al aplicar el metodo de string .split() con el valor en tipo entero
    """
    list = date.split('-')
    print(list[2])


# Desarrollado por Alexi Durán Gómez : C.C-1.067.031.983