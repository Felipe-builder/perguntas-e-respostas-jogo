from funcoes.dados.dados import *


def inicio():
    """
    -> este é o ínicio
    :return:
    """
    while True:
        escolha = menu('MENU PRINCIPAL')
        if escolha == 1:
            r = menu('JOGAR', escolha)
            arq = inicialista()
            print(r)
            if r == 1:
                criajogadores()
            if r == 2:
                lerarquivo(arq)
            comecarpartida()
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


def titulo(msg, tam=42):
    """
    -> esta função cria o cabeçalho.
    :param msg: é o conteúdo do cabeçalho a ser exebido para o usuário.
    :param tam: é o tamanho das linhas a cima e abaixo do corpo do cabeçalho.
    :return: não possui.
    """
    print('-'*tam)
    print(msg.center(tam))
    print('-' * tam)


def menu(msg_titulo, op=0):
    """
    -> função com menu ejustável na devida necessidade do programa
    :param msg_titulo: é o conteúdo do cabeçalho que vai ser enviado para a função :titulo().
    :param op: é o valor que instruir a devida chamada :proximomenu() que corpo o menu deve tomar.
    :return: retorna um valor inteiro.
    """
    opcoes = proximomenu(op)
    titulo(msg_titulo)
    escolhido = opcoesdomenu(opcoes)
    return escolhido


def opcoesdomenu(lista_op):
    """
    -> função que monta o corpo do menu ao usúario com suas opções e retorna a escolha feita para segmento do
    programa
    :param lista_op:
    :return:
    """
    cont = 1
    for item in lista_op:
        print(f'{cont} - {item}')
        cont += 1
    escolha = validadorint('Opção: ', cont-1)
    return escolha


def validadorint(msg, cont):
    while True:
        try:
            valor = int(input(msg))
        except:
            print('Digite um número inteiro!')
        else:
            if valor > cont or valor < 1:
                print(f'Digite um valor entre 1 e {cont}!')
            else:
                return valor


def proximomenu(entrada):
    """
    -> função que manda as informações necessária para montar o corpo do menu que o usúario irá interagir com
    o programa.
    :param entrada:
    :return:
    """
    if entrada == 0:
        return ['Jogar', 'Recordes', 'Instruções', 'Opções', 'Sair']
    elif entrada == 1:
        return ['Criar Jogadores', 'Carregar Jogadores', 'Partida Rápida', 'Voltar']
    elif entrada == 2:
        return ['Voltar']
    elif entrada == 3:
        return ['Voltar']
    elif entrada == 4:
        return ['Voltar']
    elif entrada == 5:
        return ['SIM', 'NÃO']


def criajogadores():
    arq = inicialista()
    nome = validadornome('Seu nome: ')
    cadastrarjogadores(arq, nome)


def inicialista():
    arq = 'lista-jogadores.txt'
    retorno = verificalista(arq)
    if not retorno:
        crialista(arq)
    return arq


def validadornome(msg):
    while True:
        try:
            nome = str(input(msg)).strip()
        except:
            print('Erro! não deixe de informar o nome!')
        else:
            return nome


def comecarpartida():
    menu('Quer começar? ', 5)
