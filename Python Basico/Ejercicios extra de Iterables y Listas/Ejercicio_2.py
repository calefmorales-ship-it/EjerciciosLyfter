my_list = []
print('Ingrese los números que desee agregar a la lista. Escriba "salir" para terminar.') 
while True:
       
    numbers = input("Ingrese un número: ")

    if numbers.lower() == "salir":
        break
    my_list.append(int(numbers))

all_positive = True

for number in my_list:
    if number <= 0:
        all_positive = False

if all_positive:    
    print ("Todos los números son positivos")  
else:
    print ("Hay al menos un número negativo o cero")   
print ("La lista de números ingresados es:", my_list)