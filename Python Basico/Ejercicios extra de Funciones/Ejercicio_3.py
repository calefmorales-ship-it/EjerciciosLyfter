def count_vowels(string):
    count = 0
    for char in string:# se recorre cada caracter de la cadena ingresada por el usuario
        if char.lower() == 'a' or char.lower() == 'e' or char.lower() == 'i' or char.lower() == 'o' or char.lower() == 'u':# el lower() se utiliza para convertir el caracter a minuscula, asi no importa si el usuario ingresa mayusculas o minusculas, el programa contara las vocales correctamente
            count += 1
    return count


print(count_vowels("HOLA MUNDO")) # prueba con mayusculas
print(count_vowels("hola mundo")) # prueba con minusculas