number_of_grades = int(input("cual es la cantidad de notas que desea ingresar: "))

grades = []

for i in range(number_of_grades):
    number = int(input("Ingrese la nota {}: ".format(i + 1)))
    grades.append(number)

print(f"Las notas ingresadas son: {grades}")

# Inicialización
approved_count = 0
failed_count = 0

sum_all = 0
sum_approved = 0
sum_failed = 0

# Recorrer la lista
for grade in grades:
    sum_all += grade

    if grade >= 70:
        approved_count += 1
        sum_approved += grade
    else:
        failed_count += 1
        sum_failed += grade

# Promedios
average_all = sum_all / number_of_grades

if approved_count > 0:
    average_approved = sum_approved / approved_count
else:
    average_approved = 0

if failed_count > 0:
    average_failed = sum_failed / failed_count
else:
    average_failed = 0

# Resultados
print("\nResultados:")
print("Aprobadas:", approved_count)
print("Desaprobadas:", failed_count)
print("Promedio total:", average_all)
print("Promedio aprobadas:", average_approved)
print("Promedio desaprobadas:", average_failed)