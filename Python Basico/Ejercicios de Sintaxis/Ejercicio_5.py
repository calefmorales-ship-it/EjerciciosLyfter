grade_counter = 1
passed_grades_count = 0
failed_grades_count = 0
passed_grades_average = 0
failed_grades_average = 0
total_grades_average = 0

total_grades = int (input("Digite la cantidad de notas a evaluar: "))
grades_counter = 0

while grades_counter < total_grades:
    current_grade = float(input(f"Digite la nota {grades_counter + 1}: "))
    if current_grade < 70:
        failed_grades_average = failed_grades_average + current_grade
        failed_grades_count += 1
    else:
        passed_grades_average = passed_grades_average + current_grade
        passed_grades_count += 1

    grades_counter += 1 

total_grades_average = total_grades_average + (current_grade / total_grades)

failed_grades_average = failed_grades_average / failed_grades_count
passed_grades_average = passed_grades_average / passed_grades_count

print("El promedio de notas aprobadas es: ", passed_grades_average)
print("El promedio de notas desaprobadas es: ", failed_grades_average)
print("El promedio de notas total es: ", total_grades_average)