from funcoes.dados.dados import *
from funcoes.logica import *


def inicio():
    """
    -> este é o ínicio. que está dentro de um loop que acabará caso o valor de retorno da função 'menu()' seja
    igual a cinco
    :return:
    """
    opcao = 0
    while True:
        escolha = menu('MENU PRINCIPAL')
        if escolha == 1:
            r = menu('JOGAR', escolha)
            arq = inicialista()
            if r == 1:
                criajogadores()  # Criar jogadores
            elif r == 2:
                lista_jogadores = lerarquivo(arq, show=True)  # Mostra qual jogador deve escolher
                jogador_escolhido, indece = escolhendo_jogador(lista_jogadores)
                pontos_carregados = int(jogador_escolhido[1])  # converte os pontos de "str" em "int"
                comecarpartida(pontos_carregados, lista_jogadores, indece, opcao)
            elif r == 3:
                criajogadores(fast=True)
            elif r == 4:
                print('voltar!!')
        elif escolha == 2:
            menu('RECORDES', escolha, v=True)
        elif escolha == 3:
            menu('INSTRUÇÕES', escolha)
        elif escolha == 4:
            r = menu('OPÇÕES', escolha)
            if r == 1:
                lista_op = ['Fácil', 'Moderado', 'Difícil']
                opcao = menu('DIFICULDADE', l_op=lista_op)
                arq_perguntas = inicialista(1, opcao)
                print(arq_perguntas)
        elif escolha == 5:
            r = menu('FINALIZANDO', escolha)
            if r == 1:
                break


def menu(msg_titulo, op=0, v=False, l_op=''):
    """
    -> função com menu ejustável na devida necessidade do programa
    :param v: se verdadeiro ele mostra o ranking.
    :param l_op: é a lista de opção das dificuldades
    :param msg_titulo: é o conteúdo do cabeçalho que vai ser enviado para a função :titulo().
    :param op: é o valor que instruir a devida chamada :proximomenu() que corpo o menu deve tomar.
    :return: retorna um valor inteiro.
    """
    opcoes = proximomenu(op)  # corpo de opções do menu a qual está contida numa lista.
    titulo(msg_titulo)  # cabeçalho do menu.
    if v:
        lerarquivo('lista-jogadores.txt', ranking=True)  # função que vai ler o arquivo com lista de jogadores
    if l_op != '':
        escolhido = opcoesdomenu(l_op)
    else:
        escolhido = opcoesdomenu(opcoes)  # cria através de um loop o corpo de opções.
    return escolhido


def opcoesdomenu(lista_op):
    """
    -> função que monta o corpo do menu ao usúario com suas opções e retorna a escolha feita para segmento do
    programa.
    :param lista_op: é a lista de opções que vai ser mostrada ao usuário.
    :return: retorna um valor inteiro para dá segmento ao programada segundo sua condição.
    """
    cont = 1
    for item in lista_op:
        print(f'{cont} - {item}')
        cont += 1
    escolha = validadorint('Opção: ', cont - 1)  # validação de dados
    return escolha


def criajogadores(fast=False):
    """
    -> vai criar um txt para guardar os dados dos jogadores.
    :param fast:caso acionando com True essa parametro determina que nenhum nome em espéfico
    será guardado.
    :return:
    """
    arq = inicialista()
    if not fast:
        nome = validadornome('Seu nome: ')
        cadastrarjogadores(arq, nome)
    else:
        cadastrarjogadores(arq)


def inicialista(procedimento=0, perguntas=0):
    """
    -> função necessária para dá inicio ao arquivo txt que irá guardar informações dos jogadores e das perguntas
    :param perguntas:
    :param procedimento: se o procedimento for 0 carrega o .txt dos jogadores, senão carrega das perguntas.
    :return:
    """
    if procedimento == 0:
        arq = 'lista-jogadores.txt'
    elif procedimento == 1:
        if perguntas == 0 or perguntas == 1:
            arq = 'perguntas-faceis.txt'
        elif perguntas == 2:
            arq = 'perguntas-medias.txt'
        elif perguntas == 3:
            arq = 'perguntas-dificeis.txt'
    retorno = verificalista(arq)
    if not retorno:
        crialista(arq)
    return arq


def comecarpartida(pontos_carregados, lista_jogadores, indice, opcao):
    resp = menu('Quer começar? ', 5)
    if resp == 1:
        arq = inicialista(1, opcao)
        lista_perguntas = carregarperguntas(arq)
        pontos = escolhendoperguntas(lista_perguntas, arq)
        pontos_carregados += pontos
        atualiza_pontos(lista_jogadores, indice, pontos_carregados)
    else:
        print('Voltando...')
