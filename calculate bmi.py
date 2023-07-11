weight = float(input('Вес '))
height = float(input('Высота '))
bmi = weight/(height**2)
if bmi <= 18.5:
    print ('Underweight')
if bmi >= 18.5 and bmi <= 25.0:
    print ('Normal')
if bmi >= 25.0 and bmi <= 30.0:
    print ('Overweight')
if bmi > 30.0:
    print ('Obese')

# def bmi(weight, height):
#     if (weight/(height**2)) <= 18.5:
#         return ('Underweight')
#     if (weight/(height**2)) >= 18.5 and (weight/(height**2)) <= 25.0:
#         return ('Normal')
#     if (weight/(height**2)) >= 25.0 and (weight/(height**2)) <= 30.0:
#         return ('Overweight')
#     if (weight/(height**2)) > 30.0:
#         return ('Obese')
# bmi(weight, height)