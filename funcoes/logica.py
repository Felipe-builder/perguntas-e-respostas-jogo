from random import shuffle, sample

pontuacao = 0


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
    """
    -> função que valida strings.
    :param msg: é o conteúdo da pergunta feita ao usuário.
    :param alternativa: se a alternativa=True, o validador vai funcionar como validação para alternativas de
    'a' até 'e', se alternativa=False, então vai funcionar para validação de qualquer nome.
    :return: vai retornar o valor de uma string.
    """
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
    """
    -> funcão que inicia o questionário.
    :param lista:
    :return:
    """
    global pontuacao
    pontuacao = 0
    mostraperguntas(lista)
    return pontuacao


def mostraperguntas(lista):
    """
    -> função que mostra o questionário.
    :param lista:
    :return:
    """
    cont = 1
    op = ['a)', 'b)', 'c)', 'd)', 'e)']
    sorteados = sistemaembaralhamento()
    for p in range(0, 8):
        repeticaomostraperguntas(lista, cont, op, sorteados)
        cont += 1


def repeticaomostraperguntas(lista, cont, op, sorteados):
    """
    -> função que
    :param lista:
    :param cont:
    :param op:
    :param sorteados:
    :return:
    """
    print(f'{cont} - {lista[0][sorteados[cont]]}')
    alternativa = lista[1][sorteados[cont]][:]
    alternativa = alternativa.split(',')
    certo = alternativa[0][:]
    shuffle(alternativa)
    for x, a in enumerate(alternativa):
        print(f'\t{op[x]} - {a[2:-2]}')
    opc_escolhida = validadornome('Qual é a certa?', alternativa=True)
    verificandoresposta(opc_escolhida, alternativa, certo)


def verificandoresposta(opc_escolhida, alternativa, cert):
    al = ['a', 'b', 'c', 'd', 'e']
    ponts = 1
    global pontuacao
    valor_opc = al.index(opc_escolhida)
    if alternativa[valor_opc] == cert:
        pontuacao += ponts
        print('certo')
    else:
        print('errado')


def sistemaembaralhamento():
    numbers = []
    for c in range(0, 25):
        numbers.append(c)
    esc = sample(numbers, 9)
    return esc
