# Proyecto_Python_DuranAlexi
# Main, entrada del proyecto
from controllers.menu_controller import *

if __name__ == '__main__':
    """Esta es la entrada principal del programa."""
    print(" _____________________________________________")
    print("|=============================================|")
    print("|========= Welcome to my Software ============|")
    print("|=============== By Alexi Dg =================|")
    print("|======= Proyecto Python S2 Campuslands ======|")
    print("|=============================================|")
    print(" --------------------------------------------- \n \n")

    program = True
    while program:
        print('=============================================')
        print('       Simulador de Gasto Diario             ')
        print('=============================================')
        print('Seleccione una opción: ')

        print('1. Registrar nuevo gasto')
        print('2. Listar gastos')
        print('3. Calcular el total de gastos')
        print('4. Generar informe de gastos')
        print('5. Salir')
        print('=============================================')
        option = int(input('> '))
        print('\n')

        if (option == 1):
            """Registrar un nuevo costo"""
            register_new_cost()
            continue 
            # La sentencia *continue* se utiliza omitir esta iteración e iniciar de nuevo en otra iteración.
            # Permitiendo así que se controle mejor el flujo y evite que en cierto caso se 
            # termine ejecutando hasta el else, devolviendo por pantalla lo programado.

        if (option == 2):
            """Ver la lista de todos los costos"""
            list_all_cost()
            continue

        if (option == 3):
            """Ver la suma del valor de todos los costos"""
            sum_all_cost()
            continue

        if (option == 4):
            """Generar un reporte con los costos"""
            generate_cost_report()
            continue


        if (option == 5):
            """Terminar la ejecución del programa"""
            program = finish_program()
            break
            # La sentencia *break* finaliza el ciclo al ser llamada.
              
        else:
            """Se ejecuta si el usuario no introduce una entrada esperada"""
            print('Por favor, elija una opción valida!!')
            continue

# Desarrollado por Alexi Durán Gómez : C.C-1.067.031.983