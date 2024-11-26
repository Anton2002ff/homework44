#Домашнее задание по шестому урок
# 1. Дан файл целых чисел, содержащий не менее четырех элементов. Вывести первый, второй, предпоследний
# и последний элементы данного файла. Если чисел меньше 3 выводить ошибку.



# def first_task(file_name):
#     with open(file_name, 'r') as file:
#         elements = file.read().split()
#
#     if len(elements) < 3:
#         print('ОШИБКА')
#     else:
#         print(elements[0], elements[1], elements[-2], elements[-1])
#
# first_task('numbs.txt')





#Задание 2
# def second_task(numb):
#     with open('numbs.txt', 'r') as file:
#         numb = file.read().split()
#
#     f1 = open('numbs3_even.txt', 'w')
#     f2 = open('numbs2_odd.txt', 'w')
#
#     for i in numb:
#         if int(i) % 2 == 0:
#             f1.write(i + '\n')
#         else:
#             f2.write(i + '\n')
#
#     f1.close()
#     f2.close()
#
#
# second_task("numbs.txt")





#Задание 3

# def third_task(file_name):
#     with open(file_name, 'r') as file:
#         elements = file.read().split()
#
#     f = open('squares.txt', 'w')
#
#     squared_numbs = [float(i) ** 2 for i in elements]
#
#     for i in squared_numbs:
#         f.write(str(i) + '\n')
#
#     f.close()
#

# third_task('numbs.txt')

#Задание 4


s = '10, 9, 8, 7, 6'
t = '5, 4, 3, 2, 1'

f = open('numbs_bin1.bin', 'wb')
f.write(s.encode('utf-8'))
f.close()

f1 = open('numbs_bin2.bin', 'wb')
f1.write(t.encode('utf-8'))
f1.close()


def fourth_task(numb_bin1, numb_bin2):
    with open(numb_bin1, 'rb') as file1:
        data1 = file1.read()
    with open(numb_bin2, 'rb') as file2:
        data2 = file2.read()

    with open('numbs_bin1.bin', 'wb') as file1:
        file1.write(data2)
    with open('numbs_bin2.bin', 'wb') as file2:
        file2.write(data1)


fourth_task('numbs_bin1.bin', 'numbs_bin2.bin')








