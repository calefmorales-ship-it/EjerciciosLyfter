number_to_multiply = int(input("Ingrese un número del 1 al 10: "))

for number in range(0, 13):
    result = number_to_multiply * number
    print(f"{number_to_multiply} x {number} = {result}")