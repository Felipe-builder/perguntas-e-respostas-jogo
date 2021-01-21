from funcoes.logica import *


# Dados dos Jogadores
def verificalista(arquivo):
    """
    -> funcao que vai verificar se tem um arquivo .txt caso não ele mesmo informa no valor de retorno False,
    :param arquivo:
    :return:
    """
    try:
        a = open(arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def crialista(arquivo):
    """
    -> esta função criará uma lista caso a função anterior "verificalista()" retornar valor False, informando
    por tanto que não há listas.
    :param arquivo: é o nome do arquivo que será criado, ou é lista com nomes de jogadores ou as perguntas
    :return:
    """
    try:
        a = open(arquivo, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {arquivo} criado com sucesso!')


def cadastrarjogadores(arquivo, nome='<Desconhecido>', pontos=0):
    """
    -> esta função vai adicionar no .txt o nome e a pontuação do jogador.
    :param arquivo: é o nome do .txt
    :param nome: é o nome do jogador, caso esse parametro seja omitido será passado o nome <Desconhecido>
    :param pontos: será sempre passado como zero, somente após pontuar no jogo que esse valor vai modificar
    :return:
    """
    try:
        a = open(arquivo, 'at')
    except:
        print('Houve um erro no cadastro')
    else:
        try:
            a.write(f'{nome};{pontos}\n')
        except:
            print('Houve um erro na escrita dos dados')
        else:
            print(f'{nome} cadastrado com sucesso!')
            a.close()


def lerarquivo(arquivo, show=False, ranking=False):
    """
    -> esta função tem por objetivo fazer uma apresentação dos dados do jogadores de forma mais apresentável e
    criar uma lista com as informações que serão modificadas ao decorrer do jogo com a pontuação deste.
    :param ranking: vem como padrão falso, caso verdadeiro mostra ao usúario o ranking.
    :param show: define se a função vai mostrar os jogadores ou não.
    :param arquivo: é o nome do arquivo
    :return: retorna uma lista com os dados de cada jogador inscrito no programa.
    """
    lista_jogadores = []
    contador = 1
    a = open(arquivo, 'r')
    for linha in a:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        if show:
            print(f'{contador} - {dado[0]:.<30}{dado[1]} pontos')
            contador += 1
        lista_jogadores.append(dado)
    if ranking:
        cria_ranking(lista_jogadores)
    a.close()
    return lista_jogadores


def atualiza_pontos(lista_jogadores, indece, pontos_carregados):
    """
    -> Funcão que ao ser chamada atualiza os pontos dos jogadores.
    :param lista_jogadores: é a lista que contem todos os dados dos jogadores cadastados, seus respectivos
    nomes e pontos.
    :param indece: é o índece do jogador que está jogando no momento e que portanto deve ter seus pontos
    atualizados.
    :param pontos_carregados: é a pontuação registrada do jogador .
    :return:
    """
    lista_jogadores[indece][1] = pontos_carregados
    arq = 'lista-jogadores.txt'
    a = open(arq, 'wt')
    for linha in lista_jogadores:
        a.write(f'{linha[0]};{linha[1]}\n')
    a.close()


# dados das perguntas!
def carregarperguntas(arquivo):
    perguntas = [[], []]
    a = open(arquivo, 'r', encoding='utf-8')
    for linha in a:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        alternativas = dado[1].split(',')
        perguntas[0].append(f'{dado[0]}')
        perguntas[1].append(f'{alternativas}')
    a.close()
    return perguntas
