def adiciona_na_mesa(peca, lista_pecas):

    nova_lista = []

    if len(lista_pecas) == 0:
        nova_lista.append(peca)

    elif len(lista_pecas) == 1:

        if peca[0] == lista_pecas[0][0]:
            peca.reverse()
            nova_lista.append(peca)
            nova_lista.append(lista_pecas[0])

        elif peca[1] == lista_pecas[0][0]:
            nova_lista.append(peca)
            nova_lista.append(lista_pecas[0])

        elif peca[0] == lista_pecas[0][1]:
            nova_lista.append(lista_pecas[0])
            nova_lista.append(peca)
        
        elif peca[1] == lista_pecas[0][1]:
            peca.reverse()
            nova_lista.append(lista_pecas[0])
            nova_lista.append(peca)

    else:

        if peca[0] == lista_pecas[0][0]:
            peca.reverse()
            nova_lista.append(peca)
            for i in range(0, len(lista_pecas)):
                nova_lista.append(lista_pecas[i])

        elif peca[1] == lista_pecas[0][0]:
            nova_lista.append(peca)
            for i in range(0, len(lista_pecas)):
                nova_lista.append(lista_pecas[i])

        elif peca[0] == lista_pecas[-1][1]:
            for i in range(0, len(lista_pecas)):
                nova_lista.append(lista_pecas[i])
            nova_lista.append(peca)
        
        elif peca[1] == lista_pecas[-1][1]:
            peca.reverse()
            for i in range(0, len(lista_pecas)):
                nova_lista.append(lista_pecas[i])
            nova_lista.append(peca)
    
    return nova_lista


    
