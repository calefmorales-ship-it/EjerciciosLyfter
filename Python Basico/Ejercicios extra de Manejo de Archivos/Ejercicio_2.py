def count_words(text):
    with open(text, 'r') as file:
        content = file.read()
        words = content.split() # dividir el contenido en palabras utilizando el espacio como separador,split() devuelve una lista de palabras
        return len(words) #len() devuelve el número de elementos en la lista, que es el número de palabras en el archivo
    

def main():
    word_count = count_words('Palabras.txt') 
    print(f'Este archivo contiene {word_count} palabras.')


if __name__ == "__main__":    
    main()