'''Você foi contratado para desenvolver um programa em Python que realiza consultas sobre a população dos municípios do Brasil com base em um arquivo CSV contendo dados do último censo do IBGE. O programa deve oferecer duas opções de consulta para o usuário:

1. Consulta por região: O programa deverá listar as 10 cidades mais populosas de cada estado dentro de uma região específica do Brasil, apresentando as populações de cada cidade e o percentual que cada população representa do total do estado;
2. Consulta por estado: O programa deverá listar as 10 cidades mais populosas de um estado escolhido, apresentando as populações de cada cidade e o percentual que cada população representa do total do estado.

INSTRUÇÕES:
i. O programa deve começar solicitando ao usuário uma das duas opções de consulta:
    i. Consultar por estado;
    ii. Consultar por região.
ii. Caso o usuário escolha consultar por região, o programa deverá:
    ii. Solicitar que o usuário informe a região do Brasil (Norte, Sul, Sudeste, Centro-Oeste, Nordeste);
    ii. Para cada estado da região, listar as 10 cidades mais populosas (nome e população);
    iii. As cidades devem ser listadas em ordem decrescente de população dentro de cada estado.
iii. Caso o usuário escolha consultar por estado, o programa deverá:
    i. Solicitar que o usuário informe a sigla de um estado;
    ii. Listar as 10 cidades mais populosas daquele estado (nome, população e percentual de cada cidade em relação à população total do estado);
    iii. As cidades devem ser listadas em ordem decrescente de população.

FORMATO DE ENTRADA:

i. O arquivo CSV a ser utilizado (CENSO_2022_POPULACAO_RESIDENTE_MUNICIPIOS.CSV)contém os seguintes campos:
    º Nome do município;
    º Código municipal;
    º UF;
    º População total.
ii. Exemplos de linhas no CSV:
    º Natal;2408102;RN;751300
    º Mossoró;2408003;RN;264577
    º UF;
Parnamirim;2403251;RN;252716

FLUXO DO PROGRAMA:

i. O programa pergunta: "Deseja consultar por região ou estado?";
ii. O programa solicita: "Informe o estado:" ou "Informe a região:";
iii. O programa exibe os dados conforme as escolhas do usuário.'''

import os, sys

# Obtendo o diretório onde o programa está salvo.
strDir = os.path.dirname(__file__)

# Ler arquivos.
try:
    arqEntrada = open(f'{strDir}\\censo_2022_populacao_residente_municipios.csv', 'r', encoding='utf-8')
    linhas = arqEntrada.readlines()
except FileNotFoundError:
    sys.exit('\nERROR: Arquivo não existe...')
except Exception as erro:
   sys.exit(f'\nERROR: {erro}...')

# criação da lista com base nos dados do censo.
dados_censo = [linha.strip().split(";") for linha in linhas[1:]]

# Organizando por estado.
norte = ["AC", "AP", "AM", "PA", "RO", "RR", "TO"]
nordeste = ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"]
centro_oeste = ["GO", "MT", "MS", "DF"]
sudeste = ["ES", "MG", "RJ", "SP"]
sul = ["PR", "RS", "SC"]

# Solicitar opção do usuário.
tipo_consulta = input("Deseja consultar por região ou estado? ").strip().lower()

# Dados por estado.
if tipo_consulta == "estado":
    estado = input("Informe a sigla do estado: ").strip().upper()
    municipios = list(filter(lambda x: x[2] == estado, dados_censo))
    
    if not municipios:
        print(f"ERRO: Estado '{estado}' não encontrado.")
    else:
        municipios = sorted(municipios, key=lambda x: int(x[3]), reverse=True)
        populacao_total_estado = sum(int(m[3]) for m in municipios)
        
        print(f"\nAs 10 cidades mais populosas do estado {estado}:")
        for municipio in municipios[:10]:
            nome = municipio[0]
            populacao = int(municipio[3])
            percentual = (populacao / populacao_total_estado) * 100
            print(f"{nome}: {populacao} habitantes ({percentual:.2f}%)")

# Dados por região.
elif tipo_consulta == "região":
    regiao = input("Informe a região (Norte, Nordeste, Centro-Oeste, Sudeste, Sul): ").strip().title()
    
    if regiao == "Norte":
        estados = norte
    elif regiao == "Nordeste":
        estados = nordeste
    elif regiao == "Centro-Oeste":
        estados = centro_oeste
    elif regiao == "Sudeste":
        estados = sudeste
    elif regiao == "Sul":
        estados = sul
    else:
        sys.exit(f"ERROR: Região '{regiao}' não encontrada.")
        estados = []

    if estados:
        print(f"\nAs 10 cidades mais populosas de cada estado na região {regiao}:")
        
        for estado in estados:
            municipios = list(filter(lambda x: x[2] == estado, dados_censo))
            
            if not municipios:
                print(f"ERRO: Estado '{estado}' não encontrado.")
                continue
            
            municipios = sorted(municipios, key=lambda x: int(x[3]), reverse=True)
            print(f"\nEstado: {estado}")
            for municipio in municipios[:10]:
                nome = municipio[0]
                populacao = int(municipio[3])
                print(f"{nome}: {populacao} habitantes")
else:
    sys.exit("ERROR: Opção inválida. Por favor, digite 'região' ou 'estado'.")

print('\n--- Fim do programa, obrigado pelo teste!"-" ---')
