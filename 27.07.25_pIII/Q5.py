'''Utilizando os arquivos GABARITO.TXT e PROVAS.CSV faça o que se pede:

i. O programa deverá ler o arquivo GABARITO.TXT e armazenar o seu conteúdo em uma lista;
ii. O programa deverá ler o arquivo PROVAS.CSV e montar uma lista com os dados contidos nesse arquivo. Observe que cada linha tem o nome do aluno e as suas opções marcadas em cada questão;
iii. O programa deverá adicionar no final de cada sub-lista do item (ii) a quantidade de acertos do aluno;
iv. Em seguida o programa deverá ordenar a lista modificada no item (iii) pela quantidade de acertos de cada aluno, começando pela maior pontuação até a menor pontuação obtida ;
v. O programa deverá salvar a lista do item (iv) no mesmo formato do arquivo PROVAS.TXT (cada aluno em uma linha, juntamebnte com suas opções marcadas e sua pontuação. Os dados dever ser separados por ;). O arquivo deverá ser salvo com o nome RESULTADOS.CSV.
'''
import os, sys

# Obtendo o diretório onde o programa está salvo.
diretorio = os.path.dirname(__file__)

# Ler arquivos.
try:
   gabLeitura = open(f'{diretorio}\\gabarito.txt', 'r', encoding='utf-8')
   provasLeitura = open(f'{diretorio}\\provas.csv', 'r', encoding='utf-8')
   arqescrita = open(f'{diretorio}\\RESULTADOS.CSV','w', encoding='utf-8')
except FileNotFoundError:
   sys.exit('\nERRO: Arquivo não encontrado...')
except Exception as erro:
   sys.exit(f'\nERRO: {erro}')

# criação das listas gabarito e provas.
else:
   lista_gabarito = list(gabLeitura.readline().split())
   lista_provas = list()

for strProva in provasLeitura: # lê linha por linha automaticamente
    strProva = strProva.strip()
    if not strProva: # ignora linhas vazias
        continue
    lstAux = [linha for linha in strProva.split(';')] # separa os dados da linha.
    lista_provas.append(lstAux)

provasLeitura.close()
gabLeitura.close()

# Inserindo notas
for prova in lista_provas:
   acertos = 0
   for nota in range(1, len(prova)): # começa de [1] pois [0] são alunos.
      if prova[nota] == lista_gabarito[nota - 1]:
         acertos += 1
   prova.append(acertos)

lista_provas.sort(key = lambda prova: prova[11], reverse = True)

# Escrever no arquivo
for prova in lista_provas:
   linha = ';'.join(str(i) for i in prova)
   arqescrita.write(f'{linha}\n')
arqescrita.close()

# Imprimir prova
for prova in lista_provas:
   print(prova)