my_list = []
print('Ingrese los números que desee agregar a la lista. Escriba "salir" para terminar.') 
while True:
       
    numbers = input("Ingrese un número: ")

    if numbers.lower() == "salir":
        break
    my_list.append(int(numbers))
new_list = []   
average = sum(my_list) / len(my_list) # sum() para sumar los elementos de la lista y len() para obtener la cantidad de elementos en la lista, lo que nos permite calcular el promedio.
for number in my_list:
    if number > average:
        new_list.append(number)
print ("El promedio de los números ingresados es:", average)
print('los numeros mayores son:', new_list)