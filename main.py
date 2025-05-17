# Proyecto_Python_DuranAlexi
# Main, entrada del proyecto

if __name__ == '__main__':
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
        option = int(input('=> '))

        if (option == 1):
            print('hola mundo')

        if (option == 2):
            print('hola mundo')

        if (option == 3):
            print('hola mundo')

        if (option == 4):
            print('hola mundo')


        if (option == 5):
            dato = input('\n¿Quieres salir del programa ? (S/N): ')

            if (dato.lower() == 's'):
                print('Gracias por utilizar el software. Bye!!')
                program = False

            elif (dato.lower() == 'n'):
                print('Gracias por utilizar el software. Bye!!')
            
            else:
                print('Por favor, elija una opción valida!!')
        
        else:
            print('Por favor, elija una opción valida!!')

# Desarrollado por Alexi Durán Gómez : C.C-1.067.031.983