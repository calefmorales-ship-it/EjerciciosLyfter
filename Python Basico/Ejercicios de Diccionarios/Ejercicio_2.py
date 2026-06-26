list_keys   = ["name", "lastName", "role"]
list_values = ["Jeremy", "Morales", "Database Administrator"]   
dictionary = {}
for i in range(len(list_keys)):
    dictionary[list_keys[i]] = list_values[i] # las listas tienen el mismo numero de elementos, por lo que se puede usar el mismo indice para ambas
print(dictionary)