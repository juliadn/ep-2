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

#para saber quais peças aparecerão para o player
pecas_jogaveis = iniciando['jogadores'][0]


#jogando

print('Mesa: ', iniciando['mesa'])
print(pecas_jogaveis)
qual_peca = int(input('Escolha a peça: ')) - 1
analise = posicoes_possiveis(iniciando['mesa'], pecas_jogaveis)

if (qual_peca + 1) in analise:
    situacao = adiciona_na_mesa(pecas_jogaveis[qual_peca], iniciando['mesa'])
    del(pecas_jogaveis[qual_peca])
else:
    if len(iniciando['monte']) > 0:
        pecas_jogaveis.append(iniciando['monte'][0])
    else:
        print('Você não possui peças e não possui peças no monte, passou a vez.')


while True:
    print('Mesa: ', situacao)
    print(pecas_jogaveis)
    qual_peca = int(input('Escolha a peça: ')) -1
    situacao = adiciona_na_mesa(pecas_jogaveis[qual_peca], situacao)
    del(pecas_jogaveis[qual_peca])
