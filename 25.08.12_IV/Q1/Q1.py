'''
a. Solicite ao usuário o ano desejado (o ano informado não pode ser superior ao ano atual, para isso deve-se usar as funções/métodos da biblioteca 
DATETIME para obter/validar o ano atual;

b. Solicite ao usuário a moeda desejada (deve haver a validação se a moeda é válida ou não com base na variável dicMoedas);

c. Com base no ano informado e na moeda informada efetuar os devidos ajustes no código para que seja feita a requisição relativa ao ano e moeda informados;

d. Deve-se criar uma função que receba como argumento uma variavel do tipo dicionário e retorne um dicionário onde as chaves serão os nomes dos meses e os respectivos 
valores serão dicionários cujas chaves serão mediaCompra e mediaVenda e os valores dessas chaves serão as médias de compra e de venda da moeda de cada mês (utilizar apenas os 
valores de fechamento da moeda em cada data para se calcular a média mensal). Fixar as médias com 3 casas decimais. Lembre de que podem ocorrer erros e sendo assim ao invés de 
retornar o dicionário deverão ser retornadas exceções com suas respectivas mensagens;

e. Uma vez que a função retotne o dicionário do item (d), deve-se salvá-lo, no formato de dicionário, em um arquivo com o nome medias_cotacoes_MMM_AAAA.json (substitua MMM pela 
sigla da moeda e AAAA pelo ano informado);

f. Deve-se criar um segundo arquivo chamado medias_cotacoes_MMM_AAAA.csv (substitua MMM pela sigla da moeda e AAAA pelo ano informado) onde a primeira linha será: moeda;mes;
mediaCompra;mediaVenda e cada linha a seguir será a sigla da moeda na primeira coluna, o nome de cada mês na segunda coluna, a média de compra (com 3 casas decimais) na 
terceira coluna e a média de venda (com 3 casas decimais) na quarta coluna, lembrando de separar cada informação por ; (ponto-e-vírgula);

g. Lembre-se de tratar as devidas exceções no programa (conversões de valores, requisições na WEB, manipulação de arquivos, ...). Elas são obrigatórias'''

import os, sys, requests, json
from Q1_funçoes import listar_moedas, calculo_medias_mensais
from datetime import datetime

ano_atual = datetime.now().year # Definir ano atual

# Solicitar ano desejado pelo usuário e validar
try:
    ano = int(input('Escolha um ano desejado para verificação: '))
    while ano > ano_atual or ano < 1994:
        ano = int(input(f'Ano inválido ( o ano deve estar entre 1994 e o ano atual ), digite novamente: '))
except ValueError:
    sys.exit('Digite um número inteiro para o ano.')
except Exception as e:
    sys.exit(f'ERR0: {e}')

# Api moedas.
strURLMoedas = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/Moedas?$top=100&$format=json'
try:
    dicMoedas = requests.get(strURLMoedas).json()
except Exception:
    sys.exit('ERR0: Não foi possível acessar a lista de moedas.')


# Listar moedas disponíveis.
lstMoedas = listar_moedas(dicMoedas)

# Solicitar uma moeda desejada.
moeda = input('Escolha a moeda desejada pela sigla (ex: USD, EUR) para verificação: ').upper()
while not moeda in lstMoedas:
    moeda = input(f'ERR0: Moeda "{moeda}" inválida, digite novamente: ').upper()

# Api cotações.
strURLCotacoes  = f'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoMoedaPeriodo(moeda=@moeda,dataInicial=@dataInicial,dataFinalCotacao=@dataFinalCotacao)?@moeda=%27{moeda}%27&@dataInicial=%2701-01-{ano}%27&@dataFinalCotacao=%2712-31-{ano}%27&$format=json'
try:    
    dicCotacoes = requests.get(strURLCotacoes).json()
except Exception:
    sys.exit('ERR0: Não foi possível acessar as cotações.')

# Calcular médias mensais.
try:
    resultado = calculo_medias_mensais(dicCotacoes)
except Exception as e:
    sys.exit(f'ERR0: {e}')

# Salvar arquivos.
strDir = os.path.dirname(__file__)

# Salvar arquivo.json.
cotacoes_json = f'{strDir}\\medias_cotacoes_{moeda}_{ano}.json'
arquivo_json = open(cotacoes_json, 'w', encoding='utf-8')
json.dump(resultado, arquivo_json, ensure_ascii=False, indent=4) # json.dump: pega um objeto Python (lista, dicionário, etc.) e grava diretamente em um arquivo.
arquivo_json.close

# Salvar arquivo.csv.
cotacoes_csv = f'{strDir}\\medias_cotacoes_{moeda}_{ano}.csv'
arquivo_csv = open(cotacoes_csv, 'w', encoding='utf-8')
arquivo_csv.write("moeda;mes;mediaCompra;mediaVenda\n")
for mes, valores in resultado.items():
    arquivo_csv.write(f"{moeda};{mes};{valores['mediaCompra']:.3f};{valores['mediaVenda']:.3f}\n")
arquivo_csv.close()

print(f'Arquivos "{cotacoes_json}" e "{cotacoes_csv}" salvos com sucesso!')
print('\n--- Fim do programa, obrigado pelo teste!"-" ---')
