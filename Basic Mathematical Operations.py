from ast import operator


operator = str(input('+ - / * '))
value1 = int(input('first number '))
value2 = int(input('second number '))

if operator == '+':
    print(value1+value2)
elif operator == '-':
    print(value1-value2)
elif operator == '*':
    print(value1*value2)
else:
    print(value1/value2)
# def basic_op(operator, value1, value2):
