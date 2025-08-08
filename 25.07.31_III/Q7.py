'''Você foi contratado para desenvolver um programa em Python que analisa uma lista de produtos de informática de uma licitação. Cada produto é representado por uma sub-lista contendo as seguintes informações:
º Nome: O nome do produto (string);
º Categoria: A categoria à qual o produto pertence: "Permanente" ou "Consumo" (string);
º Preço da Empresa A: O preço do produto na Empresa A (float);
º Preço da Empresa B: O preço do produto na Empresa B (float);
º Preço da Empresa C: O preço do produto na Empresa C (float);

A lista de produtos será alimentada a partir de um arquivo CSV (PRODUTOS_INFORMATICA.CSV), e o programa deve realizar as seguintes tarefas utilizando as funções map(), filter() e funções lambda:
1. Aplicar um desconto nos preços de todos os produtos, para a empresa escolhida pelo usuário, baseado em um valor percentual fornecido pelo usuário. Para isso, crie uma nova lista com os preços já com o desconto aplicado para a empresa escolhida;
2. Filtrar e listar os produtos. Para cada produto , a nova lista deverá conter:
i. O nome do produto
ii. A categoria do produto;
iii. O menor preço após a aplicação do desconto;
iv. O nome da empresa com o menor preço.'''

import os, sys

# Obtendo o diretório onde o programa está salvo
diretorio = os.path.dirname(__file__)

# Abrindo e lendo o arquivo
try:
   arqLeitura = open(f'{diretorio}\\PRODUTOS_INFORMATICA.CSV', 'r', encoding='utf-8')
except FileNotFoundError:
   sys.exit('\nERR0: Arquivo não encontrado...')
except Exception as erro:
   sys.exit(f'\nERR0: {erro}')
else:
   lista_Produtos = []

lstCabecalho = arqLeitura.readline().strip().split(';')

# Converte as linhas do CSV para listas com os tipos (nome, categoria, float, float, float)
lista_Produtos = list(map(
   lambda linha: [linha[0], linha[1], float(linha[2]), float(linha[3]), float(linha[4])], map(lambda l: l.strip().split(';'), arqLeitura.readlines())
   ))

arqLeitura.close()

# Solicitar dados
empresa = input('Escolha a empresa que deseja aplicar o desconto ( sendo A, B ou C ): ').strip().upper() # empresa
if empresa not in ['A', 'B', 'C']:
   sys.exit('Escolha uma empresa válida...')

try:
    desconto = float(input('Digite o desconto que deseja aplicar ( sendo 5 = 5% ): ')) # desconto
    desconto = desconto / 100
except ValueError:
    sys.exit("ERR0: Percentual inválido.")
except Exception as erro:
   sys.exit(f'\nERR0: {erro}')

# Alteração dos preços ( empresas a, b ou c ).
if empresa == 'A':
    preco_empresa = 2
elif empresa == 'B':
    preco_empresa = 3
else:
    preco_empresa = 4 # C

# Aplicação do desconto.
lista_descontados = list(map(
   lambda p: [p[0],p[1],
    round(p[2] * (1 - desconto), 2) if preco_empresa == 2 else round(p[2], 2), # uso de round(..., 2) para manter 2 casas decimais.
    round(p[3] * (1 - desconto), 2) if preco_empresa == 2 else round(p[3], 2), 
    round(p[4] * (1 - desconto), 2) if preco_empresa == 2 else round(p[4], 2),], lista_Produtos))

# Pergunta filtro por categoria
opcao_filtro = input('\n--- Deseja filtrar por categoria? Digite:\n C para Consumo\n P para Permanente\n N para Não\n: ---').strip().upper()

# Aplica filtro com filter()
produtos_filtrados = list(filter(lambda p: (opcao_filtro == 'N') or 
(opcao_filtro == 'C' and p[1].lower() == 'consumo') or (opcao_filtro == 'P' and p[1].lower() == 'permanente'), lista_descontados))

# Criação da lista com o resultado ( com nome, categoria, menor preço e empresa escolhida ).
lista_escolhida = list(map(lambda p:[p[0], p[1], min(p[2], p[3], p[4]),
['Empresa A', 'Empresa B', 'Empresa C'][[p[2], p[3], p[4]].index(min(p[2], p[3], p[4]))]], lista_descontados)) # .index retorna a posição de um valor na lista.

# Salvando arquivo RESULTADO_LICITACAO.CSV.
try:
    arqescrita = open(f'{diretorio}\\RESULTADO_LICITACAO.CSV','w', encoding='utf-8')
    arqescrita.write('Produto;Categoria;Melhor Preço;Empresa Vencedora\n')
    for linha in lista_escolhida:
        arqescrita.write(f'{linha[0]};{linha[1]};{linha[2]:.2f};{linha[3]}\n')
    arqescrita.close()
except Exception as e:
    sys.exit(f'ERRO ao salvar arquivo: {e}')
else:
    print(f'\nArquivo gerado com sucesso!')









   

