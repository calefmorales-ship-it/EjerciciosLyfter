def Upper_word(word):
    my_word = []
    with open(word, 'r') as file:
        lines = file.readlines()
        for line in lines:
            my_word.append(line.strip().upper()) #recorrer cada línea del archivo, eliminar espacios en blanco y convertir a mayúsculas, luego agregar a la lista de palabras
    return my_word  

def create_new_file(my_word):
    with open('Upper_Words.txt', 'w') as new_file:
        for word in my_word: #recorrer la lista de palabras en mayúsculas y escribir cada palabra en el nuevo archivo
            new_file.write(word + "\n")
def main():
    my_word = Upper_word('Archivo3.txt') #llamar a la función para leer el archivo original y convertir las palabras a mayúsculas
    create_new_file(my_word) #llamar a la función para crear el nuevo archivo con las palabras en mayúsculas

    with open('Upper_Words.txt', 'r') as new_file: #abrir el nuevo archivo y mostrar su contenido
        print(new_file.read())  
if __name__ == "__main__":    
    main()  