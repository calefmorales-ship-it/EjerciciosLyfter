def request_number():
    while True:
        try:
            current_number = float(input('Ingresa un numero: '))
            break   
        except ValueError:
            print('Numero invalido, intente de nuevo')
    return current_number  


def show_menu():
    print('Seleccione la operacion matematica a realizar')
    print('1. Sumar')
    print('2. Restar')
    print('3. Multiplicar')
    print('4. Dividir')
    print('5. Reiniciar')
    print('6. Salir')

def request_option():
    while True:
        try:
            option = int(input('opcion: '))  
            if option < 1 or option > 6:
                print('Opcion invalida, intente de nuevo')
                continue                  
        except ValueError:
            print('Opcion invalida, intente de nuevo')
            continue
        return option

def execute_option(option, current_number):#
    match option:
        case 1:
            try:
                number = float(input('Numero a sumar: '))
                current_number = current_number + number
            except ValueError:
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
            except ZeroDivisionError:
                print('No se puede dividir entre cero, intente de nuevo')
        case 5:
            current_number = request_number()
    return current_number

def main():
    current_number = request_number() # Solicitar el número inicial al usuario y asignarlo a la variable current_number para la funcion execute_option.
    while True:
        print('\nResultado: ', current_number) # aqui current_number llama a la variable que se actualiza con cada operación realizada en la función execute_option.
        show_menu()
        option = request_option() # Solicitar la opción al usuario y asignarla a la variable option para la función execute_option.
        if option == 6:
            break
        current_number = execute_option(option, current_number) # 


if __name__ == '__main__':
    main()
