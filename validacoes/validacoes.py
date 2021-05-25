import emoji


def vereficar_coluna(coluna):
    while coluna < 0 or coluna > 10:
        coluna = int(input("Apedeuta, Escolha as 5 colunas para colocar seu barquinho 0 e 9 "))


def vereficar_linha(linha):
    while linha < 0 or linha > 10:
        linha = int(input('Apedeuta, Escolha a posição da linha entre 0 e 9 '))



