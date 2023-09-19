text = input("Enter a string : ")

lst = list(text)

a = []
#ENCRYPTION
def listToString(s):
    str1 = ""
    for ele in s:
        str1 += ele
    return str1

for i in range(len(lst)):
    ascii = ord(lst[i])
    # print(ascii, end= " ")
    e_lev_1 = (ascii + 3)
    e_lev_2 = e_lev_1 * 2
    e_lev_3 = chr(e_lev_2)
    myfile = open('xyz.txt', 'a', encoding='utf-8')
    a.append(e_lev_3)
    cipher = listToString(a)
print(cipher)
myfile.write(cipher+"\n")


#DECRYPTION

with open("xyz.txt", "r") as f:
    d_lev_1 = f.read()
    for i in range(len(d_lev_1)):
        ascii = ord(d_lev_1[i])
        d_lev_2 = int((ascii/2))
        d = d_lev_2-3
        d_lev_3 = chr(d)
        for j in range(len(d_lev_3)):
            d_lev_4 = ord(d_lev_3[j])
#             d_lev_5 = int((d_lev_4 * 2) - (d_lev_4))
            d_lev_6 = chr(d_lev_4)
            print(d_lev_6, end="")

