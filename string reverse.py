# txt = str(input())[::-1]
# print (txt)

txt = input()
print (txt)

# реверс string
# def digitize (txt):
#     txt = list(txt)
#     print(txt)
#     txt.reverse()
#     print(txt)
#     print("".join(txt))
# digitize (txt)


# реверс list
def digitize (txt):
    txt = list(txt)
    print(txt)
    txt.reverse()
    print([int(x) for x in txt])
    # print("".join(txt))
digitize (txt)
