import random
from typing import Any

LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V','W', 'X',
           'Y', 'Z']
qt_char = 5
qt_code = 200
code_vector = []
f = open('codigos.txt', 'w')
for i in range(0, qt_code):
    verify = True  # resseta o verify
    str_code = []
    while verify:
        verify = False
        for j in range(0, qt_char):  # gera
            index = int(random.randrange(0, 26))
            str_code.append(LETTERS[index])
        for k in range(0, len(code_vector)):  # testa se ha repedido
            if str_code == code_vector[k]:
                str_code = []
                print("Repetido em " + str(k))
                verify = True  # caso repetido, gera novamente
    code_vector.append(str_code[:])
    f.write("Código de Verificação: " + "".join(str_code[:]) + "Protocolo Nº: " + str(i) + "\n")
f.close()
