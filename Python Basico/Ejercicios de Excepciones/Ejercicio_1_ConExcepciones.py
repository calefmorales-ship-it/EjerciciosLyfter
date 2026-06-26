print('Calculadora con Excepciones') # Este programa es una calculadora que permite al usuario realizar operaciones matematicas basicas (suma, resta, multiplicacion y division) con un numero inicial ingresado por el usuario. El programa utiliza excepciones para manejar errores comunes, como ingresar un valor no numerico o intentar dividir entre cero, proporcionando mensajes de error claros y permitiendo al usuario corregir su entrada sin que el programa se detenga abruptamente.
while True: # Este ciclo se repetira hasta que el usuario ingrese un numero valido
    try:
        current_number = float(input ('Ingresa un numero: '))
        break # El break hace que el ciclo se detenga si el usuario ingresa un numero valido, evitando que se ejecute el codigo que esta debajo de la excepcion
    except ValueError: # Si el usuario ingresa un valor que no se puede convertir a float, se lanzara una excepcion ValueError y se mostrara el mensaje.
        print('Numero invalido, intente de nuevo') # El programa volvera al inicio del ciclo while, permitiendo que el usuario intente ingresar un numero nuevamente.
while True:
    print ('\nResultado: ', current_number)
    print ('Escoja la operacion matematica a realizar')
    print ('1. Sumar')   
    print ('2. Restar')
    print ('3. Multiplicar')
    print ('4. Dividir')
    print ('5. Reiniciar')
    print ('6. Salir')
    try:# El bloque try se utiliza para intentar ejecutar el codigo que esta dentro de el, si se produce una excepcion, se ejecutara el bloque except.
        option = int(input('opcion: '))
    except ValueError:
        print('Opcion invalida, intente de nuevo')
        continue # el continue hace que el programa vuelva al inicio del ciclo while, evitando que se ejecute el codigo que esta debajo de la excepcion

    match option:# El match se utiliza para crear menu de opciones como este.
        case 1:
            try:
                number = float(input('Numero a sumar: '))
                current_number = current_number + number
            except ValueError:# Si el usuario ingresa un valor que no se puede convertir a float, se lanzara una excepcion ValueError y se mostrara el mensaje.
                print('Numero invalido, intente de nuevo')
        case 2:
            try:
                number = float(input('Numero a restar: '))
                current_number = current_number - number
            except ValueError:
                print('Numero invalido, intente de nuevo')
        case 3:
            try:
                number = float(input('Numero a multiplicar: '))
                current_number = current_number * number
            except ValueError:
                print('Numero invalido, intente de nuevo')
        case 4:
            try:
                number = float(input('Numero a dividir: '))
                current_number = current_number / number
            except ValueError:
                print('Numero invalido, intente de nuevo')
            except ZeroDivisionError:# Si el usuario intenta dividir entre cero, se lanzara una excepcion ZeroDivisionError y se mostrara el mensaje.
                print('No se puede dividir entre cero, intente de nuevo')
        case 5:
            while True:
                try:
                    current_number = float(input ('Ingresa un nuevo numero: ')) # Este ciclo se repetira hasta que el usuario ingrese un numero valido, permitiendo reiniciar el calculo con un nuevo numero.
                    break
                except ValueError:          
                    print('Numero invalido, intente de nuevo')
        case 6:
            break