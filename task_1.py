#Это пример создания функции:
# def sum_numbers(a, b):
#     return a + b
# result = sum_numbers(3, 5)
# print("sum_numbers:", result)

#Первое задание с домашнего задания №3
#Первая функция:
# def convert_to_integer(float_list):
#     return [int(num) for num in float_list]
# float_numbers = [-1.6, 2.99]
# integer_numbers = convert_to_integer(float_numbers)
# print(integer_numbers)


#Вторая фуекция:
# def swap_words(input_string):
#     words = input_string.split()
#     if len(words) < 2:
#         raise ValueError("Строка должна содержать как минимум два слова.")
#     swapped_string = f"{words[1]} {words[0]}"
#     return swapped_string
# input_str = "Ivanou Ivan"
# result = swap_words(input_str)
# print(result)


# Третья функция:
# def convert_to_int(*numbers):
#     return [int(num) for num in numbers]
# result = convert_to_int(-1.6, 2.99)
# print(result)