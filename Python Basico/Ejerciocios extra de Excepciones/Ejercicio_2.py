def convert_to_integer(my_list): 
    for number in my_list:
        try:
            convert = int(number)  #convertir el elemento a entero
            print(f'"{number}" convertido a número {convert}')
        except ValueError: # capturar la excepción ValueError si el elemento no se puede convertir a entero
            print(f'No se pudo convertir el elemento: "{number}"')


def main(): 
    print('Resultado:')
    my_list = ['4', 'hola', '10', '5.2']
    convert_to_integer(my_list)


if __name__ == "__main__":    
    main()