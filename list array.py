# каждое значение умножает на 2
# a = [1, 2, 3]
# print(a)
# a = [num * 2 for num in a]
# print (a)


# среднее значение в массиве
# numbers = [1, 2, 3, 4]
# # b = len(a)
# # print(b)
# # c = sum(a)
# # print(c)
# # d = c/b
# # print(d)
# # a = [num * 2 for num in a]
# # print (a)

# def find_average(numbers):
#     # a = len(numbers)
#     # b = sum(numbers)
#     # c = b/a
#     a = sum(numbers)/len(numbers)
#     print(a)
# find_average(numbers)


# # умножает каждое число массива на -1
# lst = [1, -2, 3]
# # print(lst)
# # lst = [num * (-1) for num in lst]
# # print (lst)
# def invert(lst):
#     return [num * (-1) for num in lst]
# print(invert(lst))


# возведение каждого числа массива в квадрат и сложение их с выводом результата
# numbers = [1, 5, 4]
# def square_sum(numbers):
#     # return sum([num**2 for num in numbers])
#     numbers = [num**2 for num in numbers]
#     print (numbers)
#     numbers = sum(numbers)
#     print (numbers)
# square_sum(numbers)


# сумма в массиве, если пусто,то вывод 0
# numbers = [-1]
# def sum_array(numbers):
#     numbers = sum(numbers)
#     print (numbers)
# sum_array (numbers)


# сумма положительных и вывод
# arr = [1, -4, 7, 12]
# def positive_sum(arr):
#     positive_sum = 0
#     for n in arr:
#         if n > 0:
#             positive_sum += n
#     print (positive_sum)
# positive_sum(arr)


# реверс
# r = [1, 2, 3, 6]
# def solution (r):
#     r.reverse()
#     print(r)
# solution(r)


# подсчёт чисел в массиве
# n = [5, 4, 3, 2, 2, 2, 2, 1]
# print (n)
# def reverse_seq(n):
#     sum = 0
#     for i in n:
#         if i > 0:
#             sum += 1
#     print (sum)
# reverse_seq(n)


# самое маленькое значение
arr = [34, 15, 88, 2]
def find_smallest_int(arr):
    print (min(arr))
find_smallest_int(arr)
