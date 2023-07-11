# Complementary DNA
# A = {"T": "A", "A": "T", "C": "G", "G": "C"}
dna = str(input('dna '))
def DNA_strand(dna):
    string = ''
    dict = {"T": "A", 
    "A": "T", 
    "C": "G", 
    "G": "C"
    }
#     for i, j in A.items():
#         dna = dna.replace(i, j)
#     # B = A.join(dna)
#     # print (B)
    for letter in dna:
        if letter in dict:
            string += dict[letter]
        # else:
        #     print (letter)
        # if letter == 'A':
        #     letter += 'T'
        # # print(c)
        # elif letter == 'T':
        #     letter += 'A'
        # elif letter == 'C':
        #     letter = 'G'
        # elif letter == 'G':
        #     letter = 'C'          
        # print(c)
    print(string)

DNA_strand(dna)


# def DNA_strand(dna, A):
#     # for letter in dna:
#     #     if letter != 'A':
#     #         dna = dna.replace(letter, 'T')
#         # print (dna)
#         # letters = ''
#         # bases = list(dna)
#         # for letter in bases:
#         #     if letter not in A:
#         #         return (letter)
#         #     letters = [A[dna] for dna in letter]
#         # return(''.join(letters))
#         #     if i == 'A':
#         #         i = 'T'
#         #     # print(c)
#         #     if i == 'C':
#         #         i = 'G'
#         # temp = list(dna)
#         # for i in dna:
#         #     if i == 'A':
#         #         i = 'T'
#         #     # print(c)
#         #     if i == 'C':
#         #         i = 'G'
#         #     # print(c)
#         # dna = ''.join(temp)

#     # print ('A'.join('T'*len(x) for x in dna.split('A')))
#         # print(dna)
# print (DNA_strand(dna, A))
# DNA_strand(dna, A)



