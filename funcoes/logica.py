from random import randint, shuffle


def proximomenu(entrada):
    """
    -> função que contem os valores strings que serão buscado pela funcão 'menu()' para mandar as informações
     necessária para montar o corpo do menu que o usúario irá interagir com o programa.
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


def validadornome(msg, alternativa=False):
    while True:
        try:
            nome = str(input(msg)).strip()
        except:
            print('Erro! não deixe de informar o dado!')
        else:
            if alternativa:
                if nome.lower().isalpha() and nome[0] in 'abcde':
                    return nome
                else:
                    print('Digite um valor de a) a e)')
            else:
                return nome


def validadorint(msg, cont):
    """
    -> validador de números inteiros para informar a opção escolhida pelo jogador.
    :param msg: é a natureza da pergunta que será feita.
    :param cont: é o limite de valor que pode ser colocado .
    :return:
    """
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


def escolhendoperguntas(lista):
    motraperguntas(lista)


def motraperguntas(lista):
    cont = 1
    op = ['a)', 'b)', 'c)', 'd)', 'e)']
    for p in range(0, 8):
        repeticaomostraperguntas(lista, cont, op)
        cont += 1


def repeticaomostraperguntas(lista, cont, op):
    sorteio = randint(0, 24)
    print(f'{cont} - {lista[0][sorteio]}')
    alternativa = lista[1][sorteio][:]
    alternativa = alternativa.split(',')
    certo = alternativa[0][:]
    shuffle(alternativa)
    for x, a in enumerate(alternativa):
        print(f'\t{op[x]} - {a}')
    opc_escolhida = validadornome('Qual é a certa?', alternativa=True)
    verificandoresposta(opc_escolhida, alternativa, certo)


def verificandoresposta(opc_escolhida, alternativa, cert):
    al = ['a', 'b', 'c', 'd', 'e']
    valor_opc = al.index(opc_escolhida)
    if alternativa[valor_opc] == cert:
        print('certo')
    else:
        print('errado')
