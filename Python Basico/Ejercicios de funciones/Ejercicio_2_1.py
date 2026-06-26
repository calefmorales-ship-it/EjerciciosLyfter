def greeting(name):
     print(f"Hello, {name}!")


def calculate_age(birth_year):
    greeting("Jeremy")# Llamada a la función de saludo
    return 2026 - birth_year # Retornar el valor calculado para que pueda ser utilizado fuera de la función.
    age = calculate_age(1984) # variable local a la función calculate_age


#calculate_age(1984)# solo va a mostrar el saludo, pero no se puede acceder a la variable 'age' fuera de la función por ser una variable local de función.
print(f"usted tiene {age} años.") # Esto generará un error porque 'age' no está definida en este ámbito (scope) // name 'age' is not defined

# Para acceder a la variable 'age' fuera de la función, se debe retornar su valor y asignarlo a una variable en el ámbito global.