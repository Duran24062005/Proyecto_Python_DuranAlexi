# Proyecto_Python_DuranAlexi 
# Menu Controlador: El archivo controler o controlador es un archivo creado para aislar la logica de funcionamiento del programa 
# con el objetivo de modularizarlo y que de está manera sea mucho más legible al igual que facil de modificar.
# Archivo para modularizar y guardar como funciones las opciones del menu.
from functions.functiosList import *
from db.test_data import test_db
import pprint

def register_new_cost():
    """
        Esta funcion se encarga de mostrar la parte del menú para registra un nuevo gasto.
        No recibe parametros.
        Hasta el momento no retorna nada.
    """
    print('=============================================')
    print('         Registrador Nuevo Gasto             ')
    print('=============================================')
    print('Ingrese la información del gasto: \n')

    monto = input('- Monto del gasto: ' )
    category = input('- Categoría (ej. comida, transporte, entretenimiento, otros): ')
    description = input('- Descripción (opcional): ')

    option_m = input("Ingrese ' S ' para guardar o ' C ' para cancelar: ")
    print('=============================================\n')
    print(f"El monto del gasto fue de {monto}")
    print(f'El gasto pertenece a la categoria: {category}')
    print(f'Descripción: {description}. \n')

    if (option_m.lower() == 's'):
        print('¡¡Costo guardado exitosamente!!\n')

    elif (option_m.lower() == 'c'):
        print('Costo no guardado!!\n')

    else:
        print('¡Por favor, elija una opción valida!\n')


def list_all_cost():
    """
        Esta funcion se encarga de mostrar la parte del menú para mostrar todos los gasto registrados en el sistema.
        No recibe parametros.
        Hasta el momento no retorna nada.
    """
    
    print('=============================================')
    print('                Listar Gastos                ')
    print('=============================================')
    print('Seleccione una opción para filtrar los gastos:')

    print('1. Ver todos los gastos.')
    print('2. Filtrar por categoría.')
    print('3. Filtrar por rango de fechas.')
    print('4. Regresar al menú principal.')
    print('=============================================')
    option_l = int(input('> '))

    if (option_l == 1):
        """Ver todos los gastos actuales"""
        print('\nEstos son todos los gastos:\n')
        pprint.pp(test_db[0])

    if (option_l == 2):
        """filtro por categorias"""
        print('Filtro por categoria exitoso.')

    if (option_l == 3):
        """filtro por rango de fechas"""
        print('Filtro por rango de fehcas exitoso.')

    if (option_l == 4):
        """Volver al menu principal"""
        print('\n')
        return True

    
def sum_all_cost():
    """
        Esta funcion se encarga  de mostrar el resultado de la suma de todos los gastos registrados en el sistema.
    """
    pass


def generate_cost_report():
    """
        Esta funcion se encarga mostrar la parte del menú para registra un nuevo gasto.
    """
    pass


def finish_program():
    """
        Esta función permite terminar le programa.
        No recibe parametros.
        No retorna nada.
        Detiene el programa.
    """
    dato = input('\n¿Quieres salir del programa ? (S/N): ')

    if (dato.lower() == 's'):
        print('\nGracias por utilizar el software. Bye!!')
        return False

    elif (dato.lower() == 'n'):
        print('\nEsta bien!!\n')
        return True
            
    else:
        print('Por favor, elija una opción valida!!')


# Desarrollado por Alexi Durán Gómez : C.C-1.067.031.983