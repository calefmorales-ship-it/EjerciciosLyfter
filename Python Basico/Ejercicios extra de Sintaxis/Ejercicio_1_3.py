""""""
user_number = int(input("Ingrese un número: "))
COUNTER = 1
SUM = 0
while COUNTER <= user_number:
    SUM = SUM + COUNTER         
    COUNTER += 1
print(f"La suma de los números del 1 al {user_number} es: {SUM}")
