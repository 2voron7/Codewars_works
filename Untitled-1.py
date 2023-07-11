from audioop import reverse
import re
# text = "This is an example!"
# text = "Лёха ,   попробуй   сделать эту задачу"
text = 'elbuod decaps sdrow'
print (text)

# def rev1(text):
#     res=''
#     for i in range(len(text)-1,-1,-1):
#         res+=text[i]
#     return res
# new_text = rev1(text)

# print(new_text)

# def rev2(new_text):
#     splitted_string = new_text.split()
#     return splitted_string

# print(rev2(new_text))

# new_text2 = list(reversed(rev2(new_text)))
# print(new_text2)

# str_new_text2 = ' '.join(new_text2)
# print(str_new_text2)





# my_list = [1, 'two', 'a', 4]
# print(my_list)

# my_list.reverse()  # None
# my_list  # [4, 'a', 'two', 1]
# print(my_list)

# for i in reversed(text):
#     print(i, end='')
# print('\n' + '-'*len(text))
# print(text)

# for elem in text:
#     print(elem, end=' ')
# res=' '
# for i in range(len(text)-1,-1,-1):
#     res+=text[i]
# for i in range(len(text)):
#     print(text[i])
    # text_rev = splitted_string.reverse()
    # splitted_string.append(text_rev)

# def text_reverse(text):
#     text_reverse.reverse()
#     return text
# print(text_reverse)

# def reversed1(text):
#     res=[]
#     for i in range(len(text)-1,-1,-1):
#         res.append(text[i])
#     res=''.join(res)
#     return res

# n = reversed1(text)
# print(n)

# def reversed3(text): 
#     if len(text) == 1:
#         return text
#     return text[-1] + reversed3(text[:-1])

# n = reversed3(text)
# print(n)

def reverse_words(text):
    def res1(text):
        res=''
        for i in range(len(text)-1,-1,-1):
            res+=text[i]
        return res
        
    new_text = res1(text)

    def rev2(new_text):
        splitted_string = new_text.split()
        return splitted_string

    new_text2 = list(reversed(rev2(new_text)))

    str_new_text2 = ' '.join(new_text2)
    print(str_new_text2)

    return str_new_text2
print (reverse_words(text))







