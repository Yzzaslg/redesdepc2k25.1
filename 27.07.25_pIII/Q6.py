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

import sys, os

diretorio = os.path.dirname(__file__)

try:
    arqLeitura = open(f'{diretorio}\\ALUNOS_IFRN.CSV', 'r', encoding='utf-8')
    escritaCampus = open(f'{diretorio}\\ALUNOS_IFRN_CAMPUS.csv', 'w', encoding='utf-8')
    escritaAlunos = open(f'{diretorio}\\ALUNOS_IFRN_ANO.csv', 'w', encoding='utf-8')
except ValueError:
    print('\nERRO: informe um valor válido.')
except Exception as excecao:
    sys.exit(f'\nERRO: {excecao}')
else:
    lstCampus = list()
    lstAnos = list()
    lstCursos = list()
    #lstCabecalho = arqLeitura.readline().strip().split(';')
while True:
    strLinha = arqLeitura.readline().strip()
    if not strLinha: break
    lstAux = [linha for linha in strLinha.split(';')]
    # preenchendo lstCampus
    if len(lstAux[10]) < 6:
        lstCampus.append(lstAux[10])
    # para contar apenas 1 aluno pois ha alunos com mais de uma matricula
    if lstAux[7][:4] < '2025' and lstAux[7][:4] > '1990': lstAnos.append(lstAux[7][:4])
    # preenchendo lstCursos
    lstCursos.append([lstAux[10], lstAux[5]])

# Agrupar por Campus
lstCampus.sort()
lstCampusEstat = list()
contAlunos = 0
for alunos in range(len(lstCampus)):
    if alunos + 1 < len(lstCampus) and lstCampus[alunos] == lstCampus[alunos + 1]:
        contAlunos += 1
    else:        
        lstCampusEstat.append([lstCampus[alunos], contAlunos + 1, str(round((contAlunos / len(lstCampus)) * 100, 2)) + ' %']) # add campus e quant de alunos
        contAlunos = 0
lstCampusEstat.sort(key=lambda alunos: alunos[1], reverse=True)

escritaCampus.write('Campus; Quant. de Alunos; % em relação ao total\n')
for campus in lstCampusEstat:
    linha = '; '.join(str(i) for i in campus)
    escritaCampus.write(f'{linha}\n')
escritaCampus.close()

# Agrupar por Ano
lstAnos.sort()
lstAnosEstat = list()
contAlunosAno = 0
for alunos in range(len(lstAnos)):
    if alunos + 1 < len(lstAnos) and lstAnos[alunos] == lstAnos[alunos + 1]:
        contAlunosAno += 1
    else:     
        lstAnosEstat.append([lstAnos[alunos], contAlunosAno + 1]) # add ano e quant de alunos
        contAlunosAno = 0
lstAnosEstat.sort(key=lambda alunos: alunos[1], reverse=True)

escritaAlunos.write('Ano de entrada; Quant. de Alunos\n')
for aluno in lstAnosEstat:
    linha = '; '.join(str(i) for i in aluno)
    escritaAlunos.write(f'{linha}\n')
escritaAlunos.close()

# Agrupar por cursos por Campus
escritaCursos = open(f'{diretorio}\\ALUNOS_IFRN_CAMPUS_CURSO.csv', 'w', encoding='utf-8')

# Solicita ao usuário que escolha um campus
print('Digite a sigla do Campus para visualizar os cursos.')
sigla = input('[CNAT, MO, ZL, CN, CA, NC, ZN, CAL, SGA, IP, MC, PAR, SC,\nJC, PF, AP, CANG, SPP, CM, LAJ, PAAS]: ').upper()

lstCursosTemp = list(filter(lambda campus:campus[0] == sigla, lstCursos))
lstCursosTemp.sort()
lstCursosEstat = list()
contAlunosCurso = 0
for alunos in range(len(lstCursosTemp)):
    if alunos + 1 < len(lstCursosTemp) and lstCursosTemp[alunos] == lstCursosTemp[alunos + 1]:
        contAlunosCurso += 1
    else:        
        lstCursosEstat.append([lstCursosTemp[alunos][1], contAlunosCurso + 1]) # add cursos e quant de alunos
        contAlunosCurso = 0
lstCursosEstat.sort(key=lambda alunos: alunos[1], reverse=True)

escritaCursos.write('Curso; Quant. de Alunos\n')
for aluno in lstCursosEstat:
    linha = '; '.join(str(i) for i in aluno)
    escritaCursos.write(f'{linha}\n')
escritaCursos.close()

print('\nArquivos salvos com sucesso!')
print('\n--- Fim do programa, obrigado pelo teste!"-" ---')
