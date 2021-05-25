from Interface.Jogo import jogo_init
from Interface.informacoes import infor



def menu():
    print("========================= 1: Jogar ==========================")
    print("====================== 2: Informações =======================")

    r = int(input("1 ou 2: "))
    if r == 1:
        jogo_init()
    elif r == 2:
        infor()