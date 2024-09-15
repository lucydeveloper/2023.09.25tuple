# module_1_5.py
immutable_var = (1, "colour", 2, 3.5, True) # создание неизменяемой переменной
print(immutable_var) # вывод списка
# immutable_var[0] = 2 # попытка изменить элемент, это вызовит ошибку, т.к. immutable не изменяемый кортеж
# print(immutable_var[0]) # этот код не будет выполнен
mutable_list = [1, "colour", 2, 3.5, True] # cсоздание изменяемой переменной
print(mutable_list) # вывод списка
mutable_list.extend(["Цвет"]) # изменение элемента списка
print(mutable_list) # вывод списка
