import os, sys
strDir = os.path.dirname(__file__)

try:
    arqEntrada = open(f'{strDir}\\censo_2022_populacao_residente_municipios.csv', 'r', encoding='utf-8')
    linhas = arqEntrada.readlines()
except FileNotFoundError:
    sys.exit('\nERROR: Arquivo não existe...')
except Exception as erro:
   sys.exit(f'\nERROR: {erro}...')

dados = [linha.strip().split(";") for linha in linhas[1:]]

norte = ["AC", "AP", "AM", "PA", "RO", "RR", "TO"]
nordeste = ["AL", "BA", "CE", "MA", "PB", "PE", "PI", "RN", "SE"]
centro_oeste = ["GO", "MT", "MS", "DF"]
sudeste = ["ES", "MG", "RJ", "SP"]
sul = ["PR", "RS", "SC"]

tipo_consulta = input("Deseja consultar por região ou estado? ").strip().lower()

if tipo_consulta == "estado":
    estado = input("Informe a sigla do estado: ").strip().upper()
    municipios = list(filter(lambda x: x[2] == estado, dados))
    
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
            municipios = list(filter(lambda x: x[2] == estado, dados))
            
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
