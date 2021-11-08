from time import sleep


#chamando todas as funções anteriores para serem usadas.
from adicionanamesa import adiciona_na_mesa
from cria_pecas import cria_pecas
from inicia_jogo import inicia_jogo
from soma_pecas import soma_pecas
from verifica_ganhador import verifica_ganhador
from posicoes_possiveis import posicoes_possiveis


#print inicial
print('Insper Dominó')
print('=> Design de Software')
print('Seja bem vindo ao jogo de dominó! O objetivo é ficar sem peças na mão.')
print('')
print('Vamos começar!')


#laço para o jogador escolher um número de 2-4 (se escolher outro dará erro e pedirá para ele colocar outro número.)
while True:
    numero_de_jogadores = int(input('Quantos jogadores? (2-4) '))
    if numero_de_jogadores < 2 or numero_de_jogadores > 4:
        print('Erro, tente novamente')
    else:
        break



#chamando a função que dependerá do input que derem
iniciando = inicia_jogo(numero_de_jogadores, cria_pecas())

#peças do jogador
pecas_jogaveis = iniciando['jogadores'][0]


#jogando
while len(pecas_jogaveis) > 0:
    print('Mesa: \n', iniciando['mesa'], '\n')
    print('Suas peças: \n', pecas_jogaveis, '\n')
    qual_peca = int(input('Escolha a peça: '))
    print() 
    analise = posicoes_possiveis(iniciando['mesa'], pecas_jogaveis)

    if qual_peca in analise:
        situacao = adiciona_na_mesa(pecas_jogaveis[qual_peca - 1], iniciando['mesa'])
        del(pecas_jogaveis[qual_peca - 1])

#pega do monte    
    elif qual_peca not in analise:
        test = True
        while test == True:
            i = 0
            if pecas_jogaveis[i] not in analise:
                a = False
                test == False
            else:
                print('Erro! Peça não encaixa no tabuleiro, tente outra \n \n')
                a = True
                print('Suas peças: \n \n', pecas_jogaveis, '\n \n')
                while a == True:
                    qual_peca = int(input('Escolha a peça: ')) 
                    analise = posicoes_possiveis(iniciando['mesa'], pecas_jogaveis)
                    if qual_peca in analise:
                        situacao = adiciona_na_mesa(pecas_jogaveis[qual_peca - 1], iniciando['mesa'])
                        del(pecas_jogaveis[qual_peca - 1])
                        print('Situação da mesa: \n \n ', situacao, '\n \n')
                        test = True
                        i += 1
                    else:
                        break

            if a == False:

                if len(iniciando['monte']) > 0:
                    print('Pegando do monte...')
                    sleep(2)
                    pecas_jogaveis.append(iniciando['monte'][0])
                    del(iniciando['monte'][0])
                else:
                    print('Você não possui peças e não possui peças no monte, passou a vez.')
    pecas_dos_jogadores = {}
    sit = True
    while sit == True:
        for c in range (1, numero_de_jogadores):
            print('Vez do jogador {}'.format(c + 1), '\n')
            sleep(2)
            for c2 in range(0, 6):
                analiseplayers = posicoes_possiveis(situacao, iniciando['jogadores'][c])
                if c2 in analiseplayers:
                    situacao = adiciona_na_mesa(iniciando['jogadores'][c][c2], situacao)
                    del(iniciando['jogadores'][c][c2])
                    break
                else:
                    print('\n Jogador {} pegando peças do monte...' .format(c + 1))
                    sleep(2)
                    if len(iniciando['monte']) > 0:
                        iniciando['jogadores'][c].append(iniciando['monte'][0])
                        del(iniciando['monte'][0])
                    else:
                        print('jogador{} não possui peças e não possui peças no monte, passou a vez.\n' .format(c+1))
                        sleep(2)
            pecas_dos_jogadores[c] = iniciando['jogadores'][c]
            print('Situação da mesa: \n \n ', situacao, '\n \n')
            sleep(1)
                    

        print('Suas peças: \n \n', pecas_jogaveis, '\n \n')
        qual_peca = int(input('Escolha a peça: ')) 
        analise = posicoes_possiveis(situacao, pecas_jogaveis)
        if qual_peca in analise:
            situacao = adiciona_na_mesa(pecas_jogaveis[qual_peca - 1], situacao)
            del(pecas_jogaveis[qual_peca - 1])
            print('Situação da mesa: \n \n ', situacao, '\n \n')

        elif qual_peca not in analise:
            test2 = True
            while test2 == True:
                i2 = 0
                if pecas_jogaveis[i2] not in analise:
                    a = False
                    test2 = False
                else:
                    print('Erro! Peça não encaixa no tabuleiro, tente outra \n \n')
                    a = True
                    print('Suas peças: \n \n', pecas_jogaveis, '\n \n')
                    while a == True:
                        qual_peca = int(input('Escolha a peça: ')) 
                        analise = posicoes_possiveis(situacao, pecas_jogaveis)
                        if qual_peca in analise:
                            situacao = adiciona_na_mesa(pecas_jogaveis[qual_peca - 1], situacao)
                            del(pecas_jogaveis[qual_peca - 1])
                            print('Situação da mesa: \n \n ', situacao, '\n \n')
                            test2 = True
                            i2 += 1

            if a == False:

                if len(iniciando['monte']) > 0:
                    print('Pegando do monte...')
                    sleep(2)
                    pecas_jogaveis.append(iniciando['monte'][0])
                    del(iniciando['monte'][0])
                else:
                    print('Você não possui peças e não possui peças no monte, passou a vez.')
                
        print('Situação da mesa: \n', situacao, '\n \n')
        sleep(1)
else:
    ganhador = verifica_ganhador(pecas_dos_jogadores)
    print("Vencedor(es): {}".format(ganhador) )




