import random
from typing import Any

LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
           'J', 'k', 'L', 'm', 'n', 'p',
           'r', 's', 't', 'x', 'z']
qt_char1 = 3
qt_char2 = 3
qt_char3 = 3
qt_char4 = 3
qt_char5 = 4
qt_char6 = 4
qt_char6 = 4
qt_code = 200
code_vector = []
f = open('codigos.txt', 'w')
for i in range(0, qt_code):
    verify = True  # resseta o verify
    str_code = ""
    str_code1 = []
    str_code2 = []
    str_code3 = []
    str_code4 = []
    str_code5 = []
    str_code6 = []
    while verify:
        verify = False
        for j in range(0, qt_char1):  # gera
            index = int(random.randrange(0, 19))
            str_code1.append(LETTERS[index])
        for j in range(0, qt_char2):  # gera
            index = int(random.randrange(0, 19))
            str_code2.append(LETTERS[index])
        for j in range(0, qt_char3):  # gera
            index = int(random.randrange(0, 19))
            str_code3.append(LETTERS[index])
        for j in range(0, qt_char4):  # gera
            index = int(random.randrange(0, 19))
            str_code4.append(LETTERS[index])
        for j in range(0, qt_char5):  # gera
            index = int(random.randrange(0, 19))
            str_code5.append(LETTERS[index])
        for j in range(0, qt_char6):  # gera
            index = int(random.randrange(0, 19))
            str_code6.append(LETTERS[index])
        str_code = "".join(str_code1) + " " + "".join(str_code2) + " " + \
                   "".join(str_code3) + " " + "".join(str_code4) + " " + \
                   "".join(str_code5) + " " + "".join(str_code6)
        for k in range(0, len(code_vector)):  # testa se ha repedido
            if str_code == code_vector[k]:
                str_code = []
                print("Repetido em " + str(k))
                verify = True  # caso repetido, gera novamente
    code_vector.append("".join(str_code))
    f.write(str_code + "," + str(i).zfill(5) + "\n")
f.close()
