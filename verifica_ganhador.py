def verifica_ganhador(a):
    tem_ganhador = 0
    for jogador, pecas in a.items():
        if len(pecas) == 0:
            return jogador
            tem_ganhador += 1
    if tem_ganhador == 0:
        return -1