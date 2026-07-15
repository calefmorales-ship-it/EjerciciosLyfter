def sum_values(my_list):
    total = 0 # se inicializa una variable total en 0 para acumular la suma de los números válidos.
    for element in my_list: # se itera sobre cada elemento de la lista proporcionada como argumento.
        try:  # se utiliza un bloque try-except para manejar posibles excepciones que puedan surgir al intentar convertir el elemento a un número.
            numero = float(element) # se intenta convertir cada elemento de la lista a un número flotante. Si el elemento no es un número válido, se generará una excepción ValueError.
            total += numero
            print(f"{numero} sumado correctamente")

        except ValueError:
            print(f"Elemento invalido: {element}")
    return total


def main():
    my_list = ['10', 'manzana', '5.5', '3', 'n/a']
    total = sum_values(my_list)
    print("Suma total:", total)

if __name__ == "__main__":
    main()