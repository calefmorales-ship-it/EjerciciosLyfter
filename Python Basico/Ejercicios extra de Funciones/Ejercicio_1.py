def count_char(text, char):
    result = 0
    for c in text:
        if c == char:
            result += 1
    return result

text = input('Digite una palabra: ')
char = input('Ingrese el carácter que desea buscar:')
print(f'Se ha encontrado {count_char(text, char)} veces el caracter.')