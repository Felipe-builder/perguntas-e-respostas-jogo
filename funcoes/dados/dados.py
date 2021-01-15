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
    try:
        a = open(arquivo, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {arquivo} criado com sucesso!')


def cadastrarjogadores(arquivo, nome='<Desconhecido>', pontos=0):
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


def lerarquivo(arquivo):
    a = open(arquivo, 'r')
    for linha in a:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        print(f'{dado[0]:.<30}{dado[1]} pontos')
    a.close()


# dados das perguntas!
def carregarperguntas(arquivo):
    perguntas = [[], []]
    a = open(arquivo, 'r')
    for linha in a:
        dado = linha.split(';')
        dado[1] = dado[1].replace('\n', '')
        alternativas = dado[1].split(',')
        perguntas[0].append(f'{dado[0]}')
        perguntas[1].append(f'{alternativas}')
    a.close()
    print(perguntas)
    return perguntas
