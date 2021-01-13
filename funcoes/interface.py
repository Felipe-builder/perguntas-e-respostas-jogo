from funcoes.logica import *


def inicio():
    while True:
        escolha = menu('MENU PRINCIPAL')
        if escolha == 1:
            menu('JOGAR', escolha)
        elif escolha == 2:
            menu('RECORDES', escolha)
        elif escolha == 3:
            menu('INSTRUÇÕES', escolha)
        elif escolha == 4:
            menu('OPÇÕES', escolha)
        elif escolha == 5:
            r = menu('FINALIZANDO', escolha)
            if r == 1:
                break
