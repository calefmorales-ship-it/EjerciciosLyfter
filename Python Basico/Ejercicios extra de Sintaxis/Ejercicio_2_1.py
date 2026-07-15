import random

secret_number = random.randint(1, 10)
guess = int(input("Adivina el número secreto entre 1 y 10: "))
while guess != secret_number:
    guess = int(input("Intenta de nuevo: "))
print("¡Adivinaste el número secreto!"+" El número era: " + str(secret_number))
