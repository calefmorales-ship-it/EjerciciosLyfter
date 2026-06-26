try:# este bloque de código se ejecutará y si ocurre un error, se manejará en el bloque except
    name = input('Escriba su nombre: ')

    try:
        age = int(input('Escriba su edad: '))
    except ValueError: # si el usuario ingresa algo que no se puede convertir a entero, se lanzará una excepción ValueError
        raise ValueError('La edad debe ser un número válido') # raise se utiliza para lanzar una excepción personalizada con un mensaje específico

    if name == '':
        raise ValueError('El nombre no puede estar vacio')

    for char in name:
     if char.isdigit():# el isdigit() devuelve si hay un numero en el nombre
        raise ValueError('Debe ingresar un nombre sin numeros')

    if age < 0:
        raise ValueError('La edad no puede ser negativa')

    print(f'Hola {name}, su edad es {age}')

except ValueError as e: # si ocurre una excepción ValueError, se captura y se imprime el mensaje de error
    print('Error:', e)