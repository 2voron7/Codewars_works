num = int(input('Число '))

# def summation(num):
#     sum = 0
#     while sum <= num:
#         sum = num + 1
#     print (sum)

# summation(num)

sum = 0
i = 1
while i <= num:
    sum = i + sum
    i = i + 1
print (sum) 

# def summation(num):
#     return sum(range(1,num+1))