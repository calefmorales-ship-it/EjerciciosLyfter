"""Ejercicio 1.2: Escribir un programa que solicite al usuario ingresar un tiempo en segundos y determine si es mayor, menor o igual a diez minutos. Si el tiempo es menor a diez minutos, el programa debe calcular cuántos segundos faltan para llegar a diez minutos y mostrar ese resultado al usuario."""
time_seconds = int(input("Ingrese el tiempo en segundos: "))
TEN_MINUTES = 600
if time_seconds > TEN_MINUTES:
    print("Mayor a diez minutos.")
elif time_seconds < TEN_MINUTES:
    time_seconds = TEN_MINUTES - time_seconds
    print("faltan", time_seconds, "segundos para llegar a diez minutos.")
else:
    print("Exactamente diez minutos.")
