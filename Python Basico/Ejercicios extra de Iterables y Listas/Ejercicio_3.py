my_list = []
print('Ingrese los números que desee agregar a la lista. Escriba "salir" para terminar.') 
while True:
       
    numbers = input("Ingrese un número: ")

    if numbers.lower() == "salir":
        break
    my_list.append(int(numbers))
minus_number = my_list[0]
for number in my_list:
    if number < minus_number:
        minus_number = number
print ("El número más pequeño en la lista es:", minus_number)

print ("\nLa lista de números ingresados es:", my_list)#n/ salto de línea para separar la impresión del número más pequeño y la lista de números ingresados.