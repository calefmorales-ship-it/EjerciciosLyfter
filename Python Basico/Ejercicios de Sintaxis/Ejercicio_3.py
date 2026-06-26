import random
secret_number = random.randint(1, 10)
print(secret_number) # Solo para verificar el número secreto, puedes eliminar esta línea en la versión final del juego.

guess = int(input("Adivina el número secreto entre 1 y 10: "))  
while guess != secret_number:
    guess = int(input("vuelve a intentarlo: "))
    if guess < 1 or guess > 10:
        print("¡Cuidado! El número debe estar entre 1 y 10.")
print(f"¡Felicidades! El numero secreto es = {secret_number}.")
