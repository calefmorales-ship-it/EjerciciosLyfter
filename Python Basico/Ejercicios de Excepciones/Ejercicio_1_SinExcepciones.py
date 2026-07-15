print('Calculadora sin Excepciones') 
current_number = float(input ('Ingresa un numero: '))

while True:
    print ('\nResultado: ', current_number)
    print ('Escoja la operacion matematica a realizar')
    print ('1. Sumar')   
    print ('2. Restar')
    print ('3. Multiplicar')
    print ('4. Dividir')
    print ('5. Reiniciar')
    print ('6. Salir')
    option = int(input('opcion: '))
  

    match option:
        case 1:
            number = float(input('Numero a sumar: '))   
            current_number = current_number + number
        case 2:
            number = float(input('Numero a restar: '))   
            current_number = current_number - number
        case 3:
            number = float(input('Numero a multiplicar: '))   
            current_number = current_number * number
        case 4:
            number = float(input('Numero a dividir: '))
            current_number = current_number / number
        case 5:
            current_number = 0
            current_number = float(input ('Ingresa un numero: '))
        case 6:
            break