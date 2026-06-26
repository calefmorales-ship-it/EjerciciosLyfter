name = input("¿Cuál es tu nombre? ")
last_name = input("¿Cuál es tu apellido? ")
age = int(input("¿Cuántos años tienes? "))

if age < 2:
    print(f"Hola {name} {last_name}, eres un bebé.")
elif age < 10:
    print(f"Hola {name} {last_name}, eres un niño.")
elif age < 13:
    print(f"Hola {name} {last_name}, eres un Pre-adolescente.")
elif age < 18:
    print(f"Hola {name} {last_name}, eres un Adolescente.")
elif age < 30:
    print(f"Hola {name} {last_name}, eres un Adulto joven.")
elif age < 64:
    print(f"Hola {name} {last_name}, eres un Adulto.")
else:
    print(f"Hola {name} {last_name}, eres un Adulto mayor.")