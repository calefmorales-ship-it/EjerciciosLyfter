def request_name():
    name = input("Ingrese su nombre: ")
    if name.isdigit():
        raise ValueError("El nombre no puede ser un número") # este raise lo toma el main y lo maneja en el except, para mostrar el mensaje de error al usuario.
    return name


def request_age():
    try: # La excepcion que se genera aqui puede propagar al main, y ser manejada en el except para mostrar un mensaje de error al usuario.
        age = int(input("Ingrese su edad: "))
    except ValueError:
            raise ValueError("Numero no valido")
    if age < 0:
        raise ValueError("La edad no puede ser negativa")
    return age


def main():
    try:#este try - except es para manejar las excepciones que puedan surgir al solicitar el nombre y la edad, y para asegurarse de que el programa no se detenga abruptamente debido a errores de entrada.
        name = request_name()
        age = request_age()
        print(f"Hola {name}, su edad es {age}")
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()  