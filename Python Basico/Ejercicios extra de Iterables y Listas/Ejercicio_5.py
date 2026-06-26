my_list = []
print('Ingrese 5 palabas')
for i in range(5):
    input_words = input("Ingrese la palabra {}: ".format(i + 1))
    my_list.append(input_words)
print(f"Las palabras ingresadas son: {my_list}")
new_list = []   
for word in my_list:
    if len(word) > 4:#condición para verificar si la palabra tiene más de 4 caracteres  
        new_list.append(word)#agregar la palabra a la nueva lista si cumple la condición
print(f"Las palabras con más de 4 letras son: {new_list}")