def greeting(name):
    print(f"Hello, {name}!")


def calculate_age(birth_year):
    greeting("Jeremy")# Llamada a la función de saludo y pasa un nombre como argumento.
    return 2026 - birth_year # Retornar el valor calculado para que pueda ser utilizado fuera de la función.
age = calculate_age(1984)# Asignar el valor retornado por la función a una variable en el ámbito global
print(f"Usted tiene {age} años.")
