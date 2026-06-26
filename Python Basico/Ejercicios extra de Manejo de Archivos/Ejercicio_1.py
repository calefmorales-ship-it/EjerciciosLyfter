def read_file_by_lines(path):

    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    new_list = [] # crear una nueva lista para almacenar las líneas sin espacios en blanco

    for line in lines:
        new_list.append(line.strip()) # el strip() elimina los espacios en blanco al inicio y al final de cada línea

    content = " ".join(new_list) # el join() une los elementos de la lista en una sola cadena, separándolos por un espacio

    return content

def create_new_file(content):
    # Crear nuevo archivo
    with open('NuevoArchivo.txt', 'w', encoding='utf-8') as new_file:
        new_file.write(content)

    

def main():
    content = read_file_by_lines('Archivo.txt')# llamar a la función para leer el archivo original
    create_new_file(content)# llamar a la función para crear el nuevo archivo

    # Abrir nuevo archivo y mostrarlo
    with open('NuevoArchivo.txt', 'r', encoding='utf-8') as new_file:
        print(new_file.read())

if __name__ == "__main__":      
    main()  