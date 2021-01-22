from random import shuffle, sample

pontuacao = 0


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
        return ['Dificuldade', 'Voltar']
    elif entrada == 5:
        return ['SIM', 'NÃO']


def cria_ranking(lista_jogadores):
    """
    -> função que cria um ranking, pegando a lista temporaria com as informações do jogador, e altera a ordem
    da lista segundo a pontuação de cada jogador, os maiores pontuadores ficaram no topo da lista que será
    mostrada atráves estrutura de repetição.
    :param lista_jogadores: é a lista com todas as informações do jogador
    :return:
    """
    for c in range(0, len(lista_jogadores)-1):
        for i in range(c, len(lista_jogadores)):
            if int(lista_jogadores[c][1]) < int(lista_jogadores[i][1]):
                lista_jogadores[c], lista_jogadores[i] = lista_jogadores[i], lista_jogadores[c]
    cont = 1
    for jog in lista_jogadores:
        print(f'{cont}ª - {jog[0]:.<30} {jog[1]}')
        cont += 1


def escolhendo_jogador(lista_jogadores):
    """
    -> função que seleciona um jogador buscando sua pontuação registrada e seu índice.
    :param lista_jogadores: é lista que contém as informações dos jogadores.
    :return: vai retornar os valores de pontuação do jogador selecionado e o valor do seu índice.
    """
    valorjogador_escolhido = validadorint('Escolha um jogador: ', len(lista_jogadores))
    return lista_jogadores[valorjogador_escolhido-1], valorjogador_escolhido-1


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
    :return: vai retornar um valor inteiro
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


def escolhendoperguntas(lista_perguntas, arq):
    """
    -> funcão que inicia o questionário.
    :param arq: é o nome do arquivo de perguntas que será utilizado como padrão para definir qual será o acréscimo
    da pontuação caso acerte a questão fácil ou dificil.
    :param lista_perguntas: esta é a lista de perguntas.
    :return: vai retornar o valor de pontuação do jogador
    """
    global pontuacao
    pontuacao = 0
    mostraperguntas(lista_perguntas, arq)
    return pontuacao


def mostraperguntas(lista_perguntas, arq):
    """
    -> função que mostra o questionário.
    :param arq: nome do arquivo
    :param lista_perguntas: é a lista de perguntas
    :return:
    """
    cont = 1
    op = ['a)', 'b)', 'c)', 'd)', 'e)']
    sorteados = sistemaembaralhamento()  # função de embaralhamento do indice das perguntas.
    for p in range(0, 8):
        repeticaomostraperguntas(lista_perguntas, cont, op, sorteados, arq)
        cont += 1


def repeticaomostraperguntas(lista_perguntas, cont, op, sorteados, arq):
    """
    -> função que resume a função 'mostraperguntas()'
    :param arq:
    :param lista_perguntas: é a lista que contêm as perguntas e suas respectivas alternativas
    :param cont: vai informar a ordem da pergunta
    :param op: vai informar a alternativa
    :param sorteados: é a lista que contem os índices das questões de forma sorteadas
    :return:
    """
    print(f'{cont} - {lista_perguntas[0][sorteados[cont-1]]}')
    alternativa = lista_perguntas[1][sorteados[cont-1]][:]
    alternativa = alternativa.split(',')
    certo = alternativa[0][:]  # a alternativa correta sempre será no indice 0 da do item da lista de perguntas
    shuffle(alternativa)  # embaralha os conteúdos das alternativas da variavel criada somente para isso.
    for x, a in enumerate(alternativa):
        print(f'\t{op[x]} - {a[2:-2]}')
    opc_escolhida = validadornome('Qual é a certa?', alternativa=True)
    verificandoresposta(opc_escolhida, alternativa, certo, arq)


def verificandoresposta(opc_escolhida, alternativa, cert, arq):
    """
    -> função que verifica a resposta e atribui pontos caso verdadeira.
    :param opc_escolhida: é a alternativa escolhida pelo o usuário como resposta
    :param alternativa: é o valor da alternativa que será comparada com o valor da alternativa correta
    :param cert: é o valor da alternativa correta
    :param arq: é o nome do arquivo txt de perguntas que definirá quantos potnos o jogador irá ganhar.
    caso facil ganhara 1 ponto, caso médio ganha 2, caso difícil ganha 3.
    :return:
    """
    al = ['a', 'b', 'c', 'd', 'e']
    ponts = condicao_pontuacao(arq)
    global pontuacao
    valor_opc = al.index(opc_escolhida)
    if alternativa[valor_opc] == cert:
        pontuacao += ponts
        print('Certo')
    else:
        print('Errado')


def condicao_pontuacao(arq):
    """
    -> função que define qual será o valor da pontuação do jogador segundo a dificuldade das questões.
    :param arq: é o nome do arquivo txt.
    :return: retorna o valor da pontuação.
    """
    if arq == 'perguntas-faceis.txt':
        return 1
    elif arq == 'perguntas-medias.txt':
        return 2
    elif arq == 'perguntas-dificeis.txt':
        return 3


def sistemaembaralhamento():
    """
    -> utiliza uma função sample para definir as questões que irão ser apresentadas ao usúario sem repeti-las.
    :return: vai retornar os valores sorteados que estão em uma lista.
    """
    numbers = []  # inicia a lista vázia que posteriormente será adicionada os valores
    for c in range(0, 25):
        numbers.append(c)
    esc = sample(numbers, 8)  # escolhe aleatoriamente 8 valores entre os 25 valores adicionados e coloca-os em lista.
    return esc
