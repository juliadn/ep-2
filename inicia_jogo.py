def inicia_jogo(n_jogadores, pecas):
    n_jogador = 0
    jogadores = {}
    monte = []
    mesa = []

    pecas_por_jogador = 0
    numero_de_pecas = 28
    peca_do_jogador = 0

    while n_jogador < n_jogadores:
        pecas_por_jogador += 7
        pecas_do_jogador = []
        while peca_do_jogador < pecas_por_jogador:
            pecas_do_jogador.append(pecas[peca_do_jogador])
            jogadores[n_jogador] = pecas_do_jogador
            peca_do_jogador += 1
            numero_de_pecas -= 1
        n_jogador += 1

    while numero_de_pecas > 0:
        monte.append(pecas[peca_do_jogador])
        peca_do_jogador += 1
        numero_de_pecas -= 1


    dicionario_total = {}

    dicionario_total['jogadores'] = jogadores
    dicionario_total['monte'] = monte
    dicionario_total['mesa'] = mesa

    return dicionario_total

