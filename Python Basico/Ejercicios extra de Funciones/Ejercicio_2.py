def filter_by_length(list_words, min_length):
    result = [] #Lista vacía para almacenar las palabras que cumplen con la condición
    for word in list_words:#recorremos cada palabra en la lista
        if len(word) > min_length:#Si la longitud de la palabra es mayor que el número mínimo de letras, se agrega a la lista de resultados
            result.append(word)
    return result

def main():    
    list_words = ["cielo", "sol", "maravilloso", "día"] #Lista de palabras a filtrar
    min_length = int(input("Ingrese el numero de letras minimas en la palabra: ")) #Solicitamos al usuario el numero minimo de letras
    filtered_list = filter_by_length(list_words, min_length) #Llamamos a la función para filtrar la lista de palabras
    print("Palabras con al menos", min_length, "letras:", filtered_list)


if __name__ == "__main__":
    main()