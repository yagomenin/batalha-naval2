from Interface.Jogo import jogo_init
from telas.mensagens import msg_informacao


def infor():
    msg_informacao()
    print("==========================================================")
    print("AGORA QUE SABE AS INFORMAÇÔES DO JOGO, QUE TAL UMA PARTIDA")
    r = int(input("Sim ou não: "))
    if r == 's' or r == 'S':
        jogo_init()