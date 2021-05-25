from jogadas.Ataque_jogadores import atacar_jogadores_barco
from jogadas.posicoes import botes_posicoes
from jogo.jogadores import criar_jogadores, sortear_jogador_inicial
from jogo.tabuleiro import cria_tabuleiro
from telas.jogadores import placar
from telas.mensagens import mensagem_inicializacao, msg_iniciando_ataque, msg_posisao_tabuleiros, esconder_tabuleiro
from telas.tabuleiro import mostrar_tabuleiro


def jogo_init():
    mensagem_inicializacao()
    jogador1, jogador2 = criar_jogadores()
    jogador1, jogador2 = sortear_jogador_inicial(jogador1, jogador2)
    placar(jogador1, jogador2)
    tabuleiro1 = cria_tabuleiro(jogador1)
    tabuleiro2 = cria_tabuleiro(jogador2)
    tabuleiros = tabuleiro1, tabuleiro2
    mostrar_tabuleiro(tabuleiros, 0)
    jogadores = jogador1, jogador2
    msg_posisao_tabuleiros()
    tabuleiro1 = botes_posicoes(tabuleiro1, "Porta-aviões", 3)
    tabuleiro2 = botes_posicoes(tabuleiro2, "Porta-aviões", 3)
    tabuleiros = tabuleiro1, tabuleiro2
    mostrar_tabuleiro(tabuleiros, 0)
    esconder_tabuleiro()
    mostrar_tabuleiro(tabuleiros, 1)
    msg_iniciando_ataque()
    atacar_jogadores_barco(tabuleiros, jogadores, jogador1, jogador2)
    mostrar_tabuleiro(tabuleiros, 0)