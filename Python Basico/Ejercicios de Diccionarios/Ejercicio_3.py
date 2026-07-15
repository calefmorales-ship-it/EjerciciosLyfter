employee = {'name': 'John', 'email': 'john@ecorp.com', 'access_level': 5, 'age': 28}
list_of_keys = ['access_level', 'age']
for key in list_of_keys:  #     recorre la lista de claves a eliminar
    if key in employee:  #        verifica si la clave existe en el diccionario
        employee.pop(key)  # elimina la clave y su valor del diccionario
print(employee)