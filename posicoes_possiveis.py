def posicoes_possiveis(a, b):
    posicoes = []
    n = 0
    if len(a) == 0:
        for i in b:
            posicoes.append(n)
            n += 1
    else:
        for peca in b:
            if a[0][0] in peca or a[-1][1] in peca:
                posicoes.append(b.index(peca))
    return posicoes
