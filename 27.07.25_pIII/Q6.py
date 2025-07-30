'''
A partir do arquivo ALUNOS_IFRN.CSV, fazer um programa que:

i. Montar uma lista onde cada posição deverá ser uma sub-lista. A primeira posição de cada sub-lista deverá ser a sigla do campus e a segunda a quantidade de alunos 
daquele campus, no final deverá adicionada a cada sub-lista o percentual correspondente de alunos do campus em relação ao total de alunos do IFRN (limitar a 2 casas decimais). 
Essa lista deverá ser ordenada começando pelo campus com a maior quantidade de alunos. Essa lista deverá ser salva em um arquivo chamado ALUNOS_IFRN_CAMPUS.CSV (esse arquivo 
deverá ser salvo no mesmo diretório/pasta do programa). onde cada linha deverá ser os dados de cada sub-lista separados por ponto e vírgula (;);

ii. Montar uma lista onde cada posição deverá ser uma sub-lista. A primeira posição de cada sub-lista deverá ser o ano de ingresso do aluno e a segunda posição a quantidade de 
alunos que ingressaram naquele ano. Essa lista deverá ser ordenada começando pelo ano com a maior quantidade de alunos. Essa lista deverá ser salva em um arquivo chamado 
ALUNOS_IFRN_ANO.CSV (esse arquivo deverá ser salvo no mesmo diretório/pasta do programa). onde cada linha deverá ser os dados de cada sub-lista separados por ponto e 
vírgula(;);

iii. Liste os campi, peça ao usuário para escolher um e montar uma lista onde cada posição deverá ser uma sub-lista. A primeira posição de cada sub-lista deverá ser o nome do 
curso e a segunda posição deverá ser quantidade de alunos daquele curso naquele campus. Essa lista deverá ser ordenada começando pelo curso com a maior quantidade de alunos. 
Essa lista deverá ser salva em um arquivo chamado ALUNOS_IFRN_CAMPUS_CURSO.CSV (esse arquivo deverá ser salvo no mesmo diretório/pasta do programa). onde cada linha deverá ser 
os dados de cada sub-lista separados por ponto e vírgula (;).'''

import os, sys

# Obtendo o diretório onde o programa está salvo.
diretorio = os.path.dirname(__file__)

# Ler arquivos.
try:
   alunos_ifrn_leitura = open(f'{diretorio}\\alunos_ifrn.csv', 'r', encoding='utf-8')
except FileNotFoundError:
   sys.exit('\nERR0: Arquivo não encontrado...')
except Exception as erro:
   sys.exit(f'\nERR0: {erro}')

# Criando lista