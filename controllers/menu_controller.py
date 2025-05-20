# Proyecto_Python_DuranAlexi 
# Menu Controlador: El archivo controler o controlador es un archivo creado para aislar la logica de funcionamiento del programa 
# con el objetivo de modularizarlo y que de está manera sea mucho más legible al igual que facil de modificar.
# Archivo para modularizar y guardar como funciones las opciones del menu.
from functions.functiosList import *
from tabulate import tabulate

def register_new_cost():
    """
        Esta funcion se encarga de mostrar la parte del menú para registra un nuevo gasto.
        No recibe parametros.
        # TODO
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
        success = add_new_cost(category, description, monto)
        if success:
            print('¡¡Costo guardado exitosamente!!\n')
        else: 
            print('No fue posible.')

    elif (option_m.lower() == 'c'):
        print('Costo no guardado!!\n')

    else:
        print('¡Por favor, elija una opción valida!\n')


def list_all_cost():
    """
        Esta funcion se encarga de mostrar la parte del menú para mostrar todos los gasto registrados en el sistema.
        No recibe parametros.
        # TODO
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
        if(list_costs()):
            print(tabulate(list_costs(), headers='keys', tablefmt='rounded_grid'))
        else:
            print('No hay costos registrados')

    if (option_l == 2):
        """filtro por categorias"""
        print('\nPor favor mensione la categoria: ')
        cate = input('> ')
        header = ["fecha", "categoria", "descripcion", "monto"]
        if(filter_by_category(cate)):
            print(' ')
            print(tabulate(filter_by_category(cate), headers = "keys", tablefmt='rounded_grid'))
            print('\nFiltro por categoria exitoso.\n')
        
        else:
            print('No hay datos.\n')

    if (option_l == 3):
        """filtro por rango de fechas"""
        print('\nEl formato es AA-MM-DD')
        desde = input('Desde: ')
        print('\nEl formato es AA-MM-DD')
        hasta = input('Hasta: ')
        print('\nElije para filtrar:')
        print('\t1. Por año.')
        print('\t2. Por mes.')
        print('\t3. Por día.')
        by = int(input('> '))
        ranges = filter_by_range_date(by, desde, hasta)
        if range:
            print(tabulate(ranges, headers='keys', tablefmt='rounded_grid'))
            print('Filtro por rango de fehcas exitoso.')

        else:
            print('No hay datos.\n')

    if (option_l == 4):
        """Volver al menu principal"""
        print('\n')
        return True

    
def sum_all_cost():
    """
        Esta funcion se encarga  de mostrar el resultado de la suma de todos los gastos registrados en el sistema.
        No resibe parametros.
        # TODO
        No retorna nada hasta el momento.
    """
    print('=============================================')
    print('        Calcular el total de gastos          ')
    print('=============================================')
    print('Seleccione el período de cálculo:\n')

    print('1. Calcular total diario.')
    print('2. Calcular el total semanal.')
    print('3. Calcular el total mensual.')
    print('4. Regresar al menú principal.')
    print('=============================================')
    option_s = int(input('> '))

    if (option_s == 1):
        pass

    if (option_s == 2):
        pass

    if (option_s == 3):
        pass

    if (option_s == 4):
        print('\n')
        return True


def generate_cost_report():
    """
        Esta funcion se encarga mostrar la parte del menú para mostrar el screen para generar un informe de gastos.
        No recibe parametros.
        Hasta el momento no retorna nada.
    """
    print('=============================================')
    print('         Generar Informe de Gastos           ')
    print('=============================================')
    print('Seleccione el tipo de informe:\n')

    print('1. Reporte diario')
    print('2. Informe semanal')
    print('3. Informe mensual')
    print('4. Regresar al menú principal')
    print('=============================================')
    option_p = int(input('> '))

    if (option_p == 1):
        pass

    if (option_p == 2):
        pass

    if (option_p == 3):
        pass

    if (option_p == 4):
        print('\n')
        return True


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
