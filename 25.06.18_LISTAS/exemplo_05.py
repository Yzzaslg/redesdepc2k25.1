lstAlunos = list()
lstNotas_1 = list()
lstNotas_2 = list()

while True:
    # Solicita o nome, removendo espaços em branco a esquerda e a direita.
    strNome = input('Digite um nome: ').strip()

    # Verifica se foi digitado 'fim' (compara em minúsculo) para interromper o laço.
    if strNome.lower() == 'fim':
        break

    try:
        intNota_1 = int(input('Digite a Nota 1: '))
        intNota_2 = int(input('Digite a Nota 2: '))
    except ValueError:
        print('ERRO: Informe um inteiro válido...')
    except Exception as e:
        print(f'ERRO: {e}')
    else:
        if intNota_1 < 0 or intNota_1 > 100:
            print('ERRO: Nota inválida, informe entre 0 e 100...')
        elif intNota_2 < 0 or intNota_2 > 100:
            print('ERRO: Nota inválida, informe entre 0 e 100...')
        else:
            # TODO: Adicionar o nome e as notas de alunos apenas na lista listAlunos.
            lstAlunos.append(strNome)
        