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

import sys, requests, json, Q1_funçoes
from datetime import datetime

strURLMoedas  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata'
strURLMoedas += '/Moedas?$top=100&$format=json'

dicMoedas = requests.get(strURLMoedas).json()

strURLCotacoes  = 'https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/'
strURLCotacoes += 'CotacaoMoedaPeriodo(moeda=@moeda,dataInicial='
strURLCotacoes += '@dataInicial,dataFinalCotacao=@dataFinalCotacao)?'
strURLCotacoes += '@moeda=%27USD%27&@dataInicial=%2701-01-2023%27&'
strURLCotacoes += '@dataFinalCotacao=%2712-31-2023%27&$format=json'

dicCotacoes = requests.get(strURLCotacoes).json()

ano_atual = datetime.now().year # Definir ano atual

# Solicitar ano desejado pelo usuário
ano = int(input('Escolha um ano desejado para verificação: '))
if ano > ano_atual:
    sys.exit('ERR0:Informe um ano inferior ao atual.')
else:
    for moeda in dicMoedas['value']: 
        print(moeda['simbolo'],'/',moeda['nomeFormatado']) # Listagem das moedas disponíveis.
# Solicitar uma moeda desejada
    moeda = input('Escolha a moeda desejada pela sigla (ex: USD, EUR) para verificação: ').strip().upper()

