from telas.mensagens import msg_barcos
from validacoes.validacoes import vereficar_coluna, vereficar_linha
import emoji

def botes_posicoes(tabuleiro, barco, n_c):
       vez = tabuleiro['jogador']['vez']

       if vez == True:
           area = tabuleiro['area']
           print(f"Vez do {tabuleiro['jogador']['nome']}")
           for j in range(0, n_c):
               linha = int(input(f"Escolha a linha do porta-aviões: {j + 1} "))
               vereficar_linha(linha)
               for linhas, itens in enumerate(area):
                   if linhas == linha:
                       x = area[linha]
                       coluna = int(input(f"Escolha a coluna que vc vai posicionar: {j + 1} "))
                       vereficar_coluna(coluna)
                       print('===' * 10)
                       for colunas, item in enumerate(x):
                           if colunas == coluna:
                               while x[coluna] == f' {emoji.emojize(":navio:", language="pt")}':
                                   coluna = int(input("Um barco já está poscionado nesta coordenada, tente novamente "))
                               else:
                                   x[coluna] = f' {emoji.emojize(":navio:", language="pt")}'
                               break
               if j == n_c:
                  break


       if vez == False:
           area = tabuleiro['area']
           print(f"Vez do {tabuleiro['jogador']['nome']}")
           for j in range(0, n_c):
                linha = int(input(f"Escolha a linha do porta-aviões: {j + 1} "))
                vereficar_linha(linha)
                for linhas, itens in enumerate(area):
                    if linhas == linha:
                        x = area[linha]
                        coluna = int(input(f"Escolha a coluna que vc vai posicionar: {j + 1} "))
                        vereficar_coluna(coluna)
                        print('===' * 10)
                        for colunas, item in enumerate(x):
                            if colunas == coluna:
                                while x[coluna] == f' {emoji.emojize(":navio:",language="pt")}':
                                    coluna = int(input("Um barco já está poscionado nesta coordenada, tente novamente "))
                                else:
                                    x[coluna] = f' {emoji.emojize(":navio:", language="pt")}'
                                break
                if j == n_c:
                    break

       return tabuleiro







