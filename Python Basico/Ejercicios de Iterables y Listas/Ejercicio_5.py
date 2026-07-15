print("****Por favor, ingresa 10 números.****")
numbers = []

for i in range(10):    
    number = int(input("Ingrese el numero {}: ".format(i + 1)))#format es una función que se utiliza para formatear cadenas de texto. Permite insertar valores en una cadena de texto utilizando marcadores de posición, que se representan con llaves {}. Al llamar a format(), puedes pasar los valores que deseas insertar en la cadena, y estos se reemplazarán en los marcadores de posición correspondientes.
    numbers.append(number) #append() es un método de las listas en Python que se utiliza para agregar un elemento al final de la lista.

print(f"Los numeros ingresados son: {numbers}")
if len(numbers) > 0:# len() es una función  para obtener la longitud (número de elementos) de un objeto iterable, como una lista, una cadena de texto, un diccionario, etc.
    max_number = max(numbers)# max() es una función para encontrar el valor máximo en un iterable, como una lista.  
    print(f"El número más alto es: {max_number}")