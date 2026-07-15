print("\nMenú de opciones:")
print("1. string + string → concatena dos cadenas de texto")
print("2. string + int → no es posible, se produce un error de tipo // TypeError: can only concatenate str (not \"int\") to str")
print("3. int + string → no es posible, se produce un error de tipo // TypeError: can only concatenate str (not \"int\") to str")
print("4. list + list → concatena dos listas")
print("5. string + list → no es posible, se produce un error de tipo // TypeError: can only concatenate str (not \"list\") to str")
print("6. float + int → suma un número flotante y un número entero // el resultado es un número flotante")
print("7. bool + bool → realiza una operación lógica AND o OR // el resultado depende de los valores de los booleanos")
print("8. salir ")

#    Solicitamos la opción al usuario
option = int(input("Selecciona una opción (1-8): "))

    # Siempre validamos el valor de la variable option
match option:
    case 1:
        print("Hola" + "Mundo")
    case 2:
        print("Hola" + 8) 
    case 3:
        print(6 + "Mundo")
    case 4:
        list_of_integers = [4, 7, 3, 9, 3]
        list_of_strings = ["Hello", "I'm", "A", "String", "List"]
        list_of_booleans = [True, True, False]        
        print(list_of_integers + list_of_strings) 
    case 5:
        list_of_strings = ["Hello", "I'm", "A", "String", "List"]
        print("Hello" + list_of_strings)
    case 6:
        print(10.5 + 3)
    case 7:
        is_user_active = True
        admin_permissions = False
        print(is_user_active + admin_permissions)
    case 8:
        print("Saliendo...")
    case _:
        print("Opción no válida. Por favor, selecciona una opción del 1 al 8.") 
