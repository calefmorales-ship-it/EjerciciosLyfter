def request_text():
    text = input("Ingrese una linea de texto: ")
    return text


def add_text(text):
    with open("texto.txt", "a", encoding="utf-8") as file: # Abre el archivo en modo de adición (append) y si no existe, lo crea.
        file.write(text + "\n") # Agrega una nueva línea después de cada texto ingresado


def main():
    text = request_text()
    add_text(text) 
    with open("texto.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print("Contenido del archivo:")
        print(content)

if __name__ == "__main__":
     main()
