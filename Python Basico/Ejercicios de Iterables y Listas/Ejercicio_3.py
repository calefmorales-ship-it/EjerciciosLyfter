my_list = [4, 3, 6, 1, 7, 2, 5]
if len(my_list) > 1: 
    my_list[0], my_list[-1] = my_list[-1], my_list[0]# Intercambiar el primer y último elemento con una sola línea de código
print(my_list)