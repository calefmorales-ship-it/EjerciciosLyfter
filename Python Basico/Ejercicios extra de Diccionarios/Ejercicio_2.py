employees = [
    {"name": "Carlos", "email": "carlos@empresa.com", "department": "Ventas"},
    {"name": "Ana", "email": "ana@empresa.com", "department": "TI"},
    {"name": "Luis", "email": "luis@empresa.com", "department": "Ventas"},
    {"name": "Sofía", "email": "sofia@empresa.com", "department": "RRHH"},
]   
employees_by_department={}
for employee in employees:
    if employee['department'] not in employees_by_department:
        employees_by_department[employee["department"]]= [] # diccionario[nueva_key] = valor , crea la key automáticamente si no existe
    employees_by_department[employee["department"]].append(employee) 
print(employees_by_department)