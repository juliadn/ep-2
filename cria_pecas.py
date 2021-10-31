import random

def cria_pecas():
    lista_pecas = []
    i = 0
    
    while i <= 27:
        if i <= 6:
            lista_pecas.append([i, 6])
        elif i <= 12:
            lista_pecas.append([i - 7, 5])
        elif i <= 17:
            lista_pecas.append([i - 13, 4])
        elif i <= 21:
            lista_pecas.append([i - 18, 3])
        elif i <= 24:
            lista_pecas.append([i - 22, 2])
        elif i <= 26:
            lista_pecas.append([i - 25, 1])
        elif i == 27:
            lista_pecas.append([0, 0])
        i += 1
    random.shuffle(lista_pecas)
    return lista_pecas