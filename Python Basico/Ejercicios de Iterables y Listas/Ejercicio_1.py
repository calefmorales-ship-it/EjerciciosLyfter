first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']
for i in range(len(first_list)):#range(len(first_list)) devuelve una secuencia de números desde 0 hasta el número de elementos en first_list - 1, lo que nos permite acceder a cada elemento de ambas listas utilizando el mismo índice i.
    print(f'{first_list[i]} {second_list[i]}')

