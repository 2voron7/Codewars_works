character_1 = str(input('First character: '))
character_2 = str(input('Second character: '))

# print(character_1[0].isupper())
# print(character_2[0].isupper())

# def isint_1(character_1):
#     try:
#         int(character_1)
#         return True
#     except ValueError:
#         return False
        
# def isint_2(character_2):
#     try:
#         int(character_2)
#         return True
#     except ValueError:
#         return False

# print(isint_1(character_1))
# print(isint_2(character_2))

def same_case(character_1, character_2):
    try:
        int(character_1)
        return -1
    except:
        if character_1[0].isupper() == character_2[0].isupper():
            return 1
        else:
            return 0
    
print (same_case(character_1, character_2))