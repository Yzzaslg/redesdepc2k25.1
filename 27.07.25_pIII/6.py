import os, sys

strDir = os.path.dirname(__file__)

try:
    arqEntrada = open(f'{strDir}\\alunos_ifrn.csv', 'r', encoding='utf-8')
except FileNotFoundError:
    sys.exit('\nERROR: Arquivo não existe...')
except Exception as erro:
    sys.exit(f'\nERROR: {erro}...')

try:
    all_alunos_data = []
    for linha in arqEntrada: 
        partes = linha.strip().split(';')
        if len(partes) >= 4:
            all_alunos_data.append(partes)
    arqEntrada.close()

    total_alunos = len(all_alunos_data)
    print(f"Total de alunos lidos do arquivo 'alunos_ifrn.csv': {total_alunos}")
    print("-" * 30)

    contagem_campus = {}
    for aluno_data in all_alunos_data:
        campus_sigla = aluno_data[1]
        contagem_campus[campus_sigla] = contagem_campus.get(campus_sigla, 0) + 1

    lista_campus = []
    for campus, count in contagem_campus.items():
        percentual = (count / total_alunos) * 100
        lista_campus.append([campus, count, f"{percentual:.2f}%"])

    lista_campus_ordenada = sorted(lista_campus, key=lambda x: x[1], reverse=True)

    try:
        arqCampus = open("ALUNOS_IFRN_CAMPUS.csv", 'w', encoding='utf-8')
        for item in lista_campus_ordenada:
            arqCampus.write(";".join(map(str, item)) + "\n")
        arqCampus.close()
        print(f"Dados por campus salvos em 'ALUNOS_IFRN_CAMPUS.csv'")
    except IOError as e:
        print(f"ERROR: Erro ao salvar o arquivo 'ALUNOS_IFRN_CAMPUS.csv': {e}")
    print("-" * 30)

    contagem_ano = {}
    for aluno_data in all_alunos_data:
        ano_ingresso = aluno_data[2]
        contagem_ano[ano_ingresso] = contagem_ano.get(ano_ingresso, 0) + 1

    lista_ano = []
    for ano, count in contagem_ano.items():
        lista_ano.append([ano, count])

    lista_ano_ordenada = sorted(lista_ano, key=lambda x: x[1], reverse=True)

    try:
        arqAno = open("ALUNOS_IFRN_ANO.CSV", 'w', encoding='utf-8')
        for item in lista_ano_ordenada:
            arqAno.write(";".join(map(str, item)) + "\n")
        arqAno.close()
        print(f"Dados por ano de ingresso salvos em 'ALUNOS_IFRN_ANO.CSV'")
    except IOError as e:
        print(f"ERROR: Erro ao salvar o arquivo 'ALUNOS_IFRN_ANO.CSV': {e}")
    print("-" * 30)

    campi_disponiveis = sorted(list(contagem_campus.keys()))
    print("Campi disponíveis:")
    for i, campus in enumerate(campi_disponiveis):
        print(f"{i+1}. {campus}")

    campus_escolhido = ""
    while campus_escolhido not in campi_disponiveis:
        escolha_input = input("Escolha um campus pelo nome (ex: CNAT): ").upper()
        if escolha_input in campi_disponiveis:
            campus_escolhido = escolha_input
        else:
            print("Campus inválido. Por favor, escolha um campus da lista.")

    print(f"Você escolheu o campus: {campus_escolhido}")

    contagem_curso_campus = {}
    for aluno_data in all_alunos_data:
        if aluno_data[1] == campus_escolhido:
            nome_curso = aluno_data[3]
            contagem_curso_campus[nome_curso] = contagem_curso_campus.get(nome_curso, 0) + 1

    lista_curso_campus = []
    for curso, count in contagem_curso_campus.items():
        lista_curso_campus.append([curso, count])

    lista_curso_campus_ordenada = sorted(lista_curso_campus, key=lambda x: x[1], reverse=True)

    try:
        arqCursoCampus = open("ALUNOS_IFRN_CAMPUS_CURSO.CSV", 'w', encoding='utf-8')
        for item in lista_curso_campus_ordenada:
            arqCursoCampus.write(";".join(map(str, item)) + "\n")
        arqCursoCampus.close()
        print(f"Dados de cursos para '{campus_escolhido}' salvos em 'ALUNOS_IFRN_CAMPUS_CURSO.CSV'")
    except IOError as e:
        sys.exit(f"ERROR:Erro ao salvar o arquivo 'ALUNOS_IFRN_CAMPUS_CURSO.CSV': {e}")
    print("-" * 30)

except Exception as e:
    sys.exit({e})
