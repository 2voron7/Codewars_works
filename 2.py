import re

sentence = "4of Fo1r pe6ople g3ood th5e the2"
arrsent = sentence.split()
print (arrsent)

a = [re.sub('\D+', '', i) for i in arrsent]
# a.sort(key=lambda x: x)
print (a)
b = arrsent.sort(key=lambda x: x == int())

# b = arrsent.sort(key=lambda x: x[:] == int())
print (b)
# print(arrsent)