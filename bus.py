cap = int(input ('Вместимость автобуса '))
on = int(input ('Количество людей в автобусе '))
wait = int(input ('Количество людей ожидающих посадку '))
# c = cap - on
# print(c)

if cap - on >= wait:
    print ('Вместится', cap - on, 'людей')
elif cap - on < wait:
    print ('Надо подождать', wait-(cap-on))


# def enough (cap, on, wait):
#     if c > wait:
#         return ('Вместится', c, 'людей')
#     elif c < wait:
#         return ('Нет места')
#     else:
#         return ('0')

# def enough(cap, on, wait):
#     return max(0, wait - (cap - on))