import re

string = "qq2q aaa3a bbb1b zcafada4d afadsf8 asdasd7dasgt adsynhuyu5 asdnmyu6jhmyuku"
print(string)

def sort_string(string):
   splitted_string = string.split() 
   splitted_string.sort(key=lambda x: (re.search(r'\d+', x).group()))
   return ' '.join(splitted_string)

sort_string(string)
print(sort_string(string))