def check_prime_numbers(numbers_list):
    prime_numbers_list = [] 
    for number in numbers_list: # recorre cada numero de la lista.
       if number > 1:#ingnora los números menores o iguales a 1, ya que no son primos.
            for i in range(2, number): # recorre el numero desde el 2 hasta el numero-1.
                if (number % i) == 0:# si el numero es divisible por cualquier numero entre 2 y el numero-1, entonces no es primo, y se rompe el ciclo(break).
                    break
            else:# si el numero no es divisible por ningún numero entre 2 y el numero-1, entonces es primo.
                prime_numbers_list.append(number) # se agrega el numero primo a la lista de numeros primos.
    return prime_numbers_list # se devuelve la lista de numeros primos encontrados en la lista original.   



def main():
    print("****Por favor, ingresa 7 números.****")

    numbers_list = []

    for i in range(7):    
        number = int(input("Ingrese el numero {}: ".format(i + 1)))
        numbers_list.append(number)

    print("Los números ingresados son: ", numbers_list)

    check_prime_numbers_result = check_prime_numbers(numbers_list)
    print("Los números primos en la lista son: ", check_prime_numbers_result)   


if __name__ == "__main__": # Esto asegura que la función main() se ejecute solo cuando este script se ejecute directamente, y no cuando se importe como un módulo en otro script.
    main()