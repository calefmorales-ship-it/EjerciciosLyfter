my_list = []
print('Ingrese los números que desee agregar a la lista. Escriba "salir" para terminar.') 
while True:
       
    numbers = input("Ingrese un número: ")

    if numbers.lower() == "salir":
        break
    my_list.append(int(numbers))
find_number = int(input("Ingrese un número para buscar en la lista: "))
count = my_list.count(find_number)#count() es un método de las listas que cuenta cuántas veces aparece un elemento específico en la lista.
if count > 0:
    print(f"El número {find_number} se encuentra en la lista y aparece {count} veces.")

print ("La lista de números ingresados es:", my_list)

