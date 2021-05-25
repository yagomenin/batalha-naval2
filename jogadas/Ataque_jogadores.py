from telas.jogadores import placar, placar_durante_game
from telas.tabuleiro import mostrar_tabuleiro
from validacoes.validacoes import vereficar_linha, vereficar_coluna
import emoji



def atacar_jogadores_barco(tabuleiros, jogadores, jg1, jg2):
    bomba = print(emoji.emojize(':bomb:'))
    terminar = 0
    tabuleiros_destruidos = []
    jogador1 = jg1
    jogador2 = jg2
    for jogador in jogadores:
        jogo_em_andamento = True
        while jogo_em_andamento:
            if jogador1['vez'] == True:
                jogador = jg1
            elif jogador2['vez'] == True:
                jogador = jg2
            while jogador['vez'] == True:
                tabuleiro = buscar_area_para_atacar(jogador, tabuleiros)
                linha = int(input(f"{jogador['nome']} escolha uma linha para atacar: 0 e 9 "))
                vereficar_linha(linha)
                for linhas, itens_linha in enumerate(tabuleiro):
                    if linha == linhas:
                        indice_linha = tabuleiro[linha]
                        coluna = int(input(f"{jogador['nome']}, escolha a coluna que deseja jogar a bomba: 0 a 9 "))
                        vereficar_coluna(coluna)
                        for colunas, itens_coluna in enumerate(indice_linha):
                            if colunas == coluna:
                                indice_coluna = indice_linha[coluna]
                                if indice_coluna == f' {emoji.emojize(":navio:", language="pt")}':
                                    print(f"Você acertou um barco e ele afundou com sucesso , pode jogar novamente {jogador['nome']}")
                                    indice_coluna = f' {emoji.emojize(":bomba:", language="pt")}'
                                    jogador['pontos'] += 1
                                    print('====' * 10)
                                else:
                                    print(f"Você errou {jogador['nome']}")
                                    mudar_vez(jogador1, jogador2)
                                    print('====' * 10)
                                    placar_durante_game(jogador1, jogador2)
                                    print('====' * 10)
                if jogador['pontos'] == 3:
                    print('================= PARABENS =====================')
                    print(f"{jogador['nome']}, voçê ganhou no batalha naval, espero que tenha se divertido muito!!!!")
                    print(f"Você ganhou e seus pontos forma de {jogador['pontos']} ")
                    terminar = jogador['pontos']
                    placar_durante_game(jogador1, jogador2)
                    print("E ESSE FOI O PLACAR DO JOGO.")
                    tabuleiros_destruidos.append(tabuleiros)
                    break
            if terminar == 3:
                jogo_em_andamento = False
        break


    return tabuleiros_destruidos












def buscar_area_para_atacar(jogador, tabuleiros):
    for tabuleiro in tabuleiros:
        if tabuleiro['jogador']['id'] != jogador['id']:
            area = tabuleiro['area']
    return area



def mudar_vez(jogador1, jogador2):
    if jogador1['vez'] == False:
        jogador1['vez'] = True
        jogador2['vez'] = False


    elif jogador2['vez'] == False:
        jogador1['vez'] = False
        jogador2['vez'] = True















