def titulo(msg, tam=42):
    print('-'*tam)
    print(msg.center(tam))
    print('-' * tam)


def opcoesdomenu(lista_op):
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


def menu(msg_titulo, op=0):
    opcoes = proximomenu(op)
    titulo(msg_titulo)
    escolhido = opcoesdomenu(opcoes)
    return escolhido


def proximomenu(entrada):
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
