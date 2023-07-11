n = int(input('Введите количество чисел в списке '))
n += 1
# a = 2

m = list(range(1, n))
# h = [a for _ in range(n)]
# n = sum(m)
print(m)
for num in m:
    x = m[num] * num
    m.append(x)
print (m)
# def multiply(m):
#     a = 1
#     for el in m:
#         a *= el
#     return a
# print(multiply(m))
print(m)

# print(h)

# c = [x**y for x, y in zip(h, m)]
# print(c)

# c = [2**x for x in range(n+1)]
# print(c)

# item = 2
# a = [[], [], []]
# # for el in a:
# #     el.append(2)
# for i, item in enumerate(a):
#     a[i] = int(2)

# print(a)

# for i in range(len(array)):
#     array[i] = int(array[i])
# array = int(input())
# array = [int(elem) for elem in array]
# result_array = []
# for elem in array:
#     result_array.append(int(elem))
# array = result_array

# print(result_array)

# array = ['10', '11', '12']
# link = array
# print(array, link)    # ['10', '11', '12'] ['10', '11', '12']
# for i, elem in enumerate(array):
#     array[i] = int(elem)
# print(array, link)    # [10, 11, 12] [10, 11, 12]


