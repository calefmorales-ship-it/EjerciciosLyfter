def sum_numbers(numers_list):
    total = 0 # variable local de la función sum_numbers, se inicializa en 0 para acumular la suma de los números en la lista.
    for number in numers_list:
        total += number
    return total


def main():# este es el entry point del programa, donde se ejecuta la lógica principal. En este caso, se crea una lista de números y se llama a la función sum_numbers para obtener la suma de esos números, luego se imprime el resultado.
    numbers_list = [4, 6, 2, 29] 
    sum_result = sum_numbers(numbers_list)
    print(f"La suma de los números en la lista es: {sum_result}")

    
if __name__ == "__main__": # Esto asegura que la función main() se ejecute solo cuando este script se ejecute directamente, y no cuando se importe como un módulo en otro script.
    main()