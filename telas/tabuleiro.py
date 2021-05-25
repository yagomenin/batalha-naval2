from time import sleep
import emoji

from utils.fonte_cor import adiciona_cor


def mostrar_tabuleiro(tabuleiros, hide):
    oceano = emoji.emojize(':onda:', language='pt')
    for (i), tabuleiro in enumerate(tabuleiros):
        id_jogador = tabuleiro['jogador']['id']
        area = tabuleiro['area']
        for j, linha in enumerate(area):
            if j == 0 and id_jogador == 1:
                mostrar_indice_coluna(len(linha))
            mostrar_indice_linha(j)
            for posicao in linha:
                cor = '31m' if id_jogador == 1 else '34m'
                if hide == 0:
                    valor = posicao if posicao else f" {emoji.emojize(':onda:', language='pt')}"
                    print(f'{adiciona_cor(cor,  valor )}', end=' ')
                else:
                    valor = f' {oceano}'
                    print(f'{adiciona_cor(cor, valor)}', end=' ')
            print()
            if j == len(area) - 1 and id_jogador == 2:
                mostrar_indice_coluna(len(linha))
            sleep(0.05)
        if i == 0:
            print(' = ' * 13)




def mostrar_indice_coluna(tamanho_linha):
    for count in range(0, tamanho_linha):
        end = '\n' if count == tamanho_linha - 1 else ' '
        espaco_extra = ' ' if count == 0 else ''
        print(f'{espaco_extra} {adiciona_cor("33m", count)} ', end=end)


def mostrar_indice_linha(indice):
    print(adiciona_cor("33m", indice), end=':')

def tabu(tabuleiros):
    i = tabuleiros['jogador']['id']
    cor = '31m'
    area = (tabuleiros['area'])
    for j, linha in enumerate(area):
        for posicao in linha:
            print(f'{adiciona_cor(cor, posicao)}', end=' ')
        print()
        sleep(0.05)
        if i == 1:
            print(' = ' * 13)
            break

