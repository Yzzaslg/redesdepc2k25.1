'''Utilizando os arquivos GABARITO.TXT e PROVAS.CSV faça o que se pede:

i. O programa deverá ler o arquivo GABARITO.TXT e armazenar o seu conteúdo em uma lista;
ii. O programa deverá ler o arquivo PROVAS.CSV e montar uma lista com os dados contidos nesse arquivo. Observe que cada linha tem o nome do aluno e as suas opções marcadas em cada questão;
iii. O programa deverá adicionar no final de cada sub-lista do item (ii) a quantidade de acertos do aluno;
iv. Em seguida o programa deverá ordenar a lista modificada no item (iii) pela quantidade de acertos de cada aluno, começando pela maior pontuação até a menor pontuação obtida ;
v. O programa deverá salvar a lista do item (iv) no mesmo formato do arquivo PROVAS.TXT (cada aluno em uma linha, juntamebnte com suas opções marcadas e sua pontuação. Os dados dever ser separados por ;). O arquivo deverá ser salvo com o nome RESULTADOS.CSV.
'''
import os, sys

# Obtendo o diretório onde o programa está salvo
strDir = os.path.dirname(__file__)

# Abrindo e lendo o arquivo gabarito.txt
try:
   arqLeitura = open(f'{strDir}\\gabarito.txt', 'r', encoding='utf-8')
except FileNotFoundError:
   sys.exit('\nERRO: Arquivo não encontrado...')
except Exception as erro:
   sys.exit(f'\nERRO: {erro}')
else:
   lista_gabarito = []

print(lista_gabarito)

# Abrindo e lendo o arquivo provas.csv
try:
   arqLeitura = open(f'{strDir}\\provas.csv', 'r', encoding='utf-8')
except FileNotFoundError:
   sys.exit('\nERRO: Arquivo não encontrado...')
except Exception as erro:
   sys.exit(f'\nERRO: {erro}')
else:
   lista_provas = []

print(lista_provas)
