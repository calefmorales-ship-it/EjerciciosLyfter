
year = 2026

def greeting(name):
     print(f"Hello, {name}!")


def calculate_age():
    greeting("Jeremy")# Llamada a la función de saludo
    #global year # Declaración de la variable 'year' como global para poder modificarla dentro de la función.
    year= year - 1984 # inteto de modificar la variable global 'year' dentro de la función calculate_age.


calculate_age()
print(f'usted tiene {year} años.') # generará un error porque 'year' no está definida en este ámbito (scope) // UnboundLocalError: local variable 'year' referenced before assignment

# para solucionar este error, se debe declarar la variable 'year' como global dentro de la función calculate_age() para que pueda ser modificada dentro de la función y reflejar el cambio en el ámbito global.