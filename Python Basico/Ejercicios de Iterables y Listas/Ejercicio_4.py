my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = []
for value in my_list:
    if value % 2 == 0:
        new_list.append(value)
print("Lista original:", my_list)
print("Lista final:", new_list)