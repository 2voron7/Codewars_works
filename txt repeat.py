string = input()
repeat = input ()
def repeat_str (repeat, string):
    txt_n = list(string) * int(repeat)
    txt_n = "".join(txt_n)
# txt_n = (int(n) for n in txt)
    print (txt_n)

repeat_str (repeat, string)

