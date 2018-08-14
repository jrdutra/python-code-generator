import random
from typing import Any

LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V','W', 'X',
           'Y', 'Z']
qt_char = 1
qt_code = 10
code_vector = []
verify = True
for i in range(0, qt_code):
    str_code = []
    while virify:
        # gera
        for j in range(0, qt_char):
            index = int(random.randrange(0, 26))
            str_code.append(LETTERS[index])
        # testa se ha repedido
        for k in range(0, len(code_vector)):
            if str_code == code_vector[k]:
                print("Repetido em " + str(k))

    code_vector.append(str_code[:])
print(code_vector)
print(len(code_vector))
