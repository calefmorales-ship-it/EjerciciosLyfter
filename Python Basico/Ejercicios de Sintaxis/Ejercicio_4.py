number_one = int(input("Ingrese el primer número: "))
number_two = int(input("Ingrese el segundo número: "))
number_three = int(input("Ingrese el tercer número: "))

if number_one > number_two and number_one > number_three:
    print("El número mayor es: ", number_one)
elif number_two > number_one and number_two > number_three:
    print("El número mayor es: ", number_two)
else:
    print("El número mayor es: ", number_three)