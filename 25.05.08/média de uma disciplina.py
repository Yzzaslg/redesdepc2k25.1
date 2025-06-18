# PROGRAMA PARA CALCULAR A MÉDIA DE UMA DISCIPLINA SEMESTRAL NO IFRN.

# AS NOTAS DEVEM SER INTEIRAS E ENTRE 0 E 100 (INCLUSIVE).

# CASO A MÉDIA SEJA IGUAL OU SUPERIOR A 60 O ALUNO ESTARÁ
# APROVADO; CASO A MÉDIA SEJA IGUAL OU SUPERIOR A 20 O ALUNO
# ESTARÁ EM PROVA FINAL E OS DEMAIS CASOS O ALUNO ESTARÁ REPROVADO.


import sys

# Informando a nota da Etapa 1
etapa1 = int(input('Informe a nota da etapa 1(0-100):'))
if etapa1 < 0 or etapa1 > 100:
    sys.exit('ERRO: Nota etapa 1 Inválida. Informe nota entre 0 e 100.')

# Informando a nota da Etapa 2
etapa2 = int(input('Informe a nota da Etapa 2(0-100): '))
if etapa2 < 0 or etapa2 > 100:
    sys.exit('ERRO: Nota Etapa 2 Inválida. Informe nota entre 0 e 100.')

# Calculando a média
media = int(round((etapa1 * 2 + etapa2 * 3) / 5))
print(f'Média do Aluno: {media}')

# Verificando a situação do aluno
if media >= 60:
    print('Aluno Aprovado.')
elif media >= 20:
    print('Aluno em Prova Final.')
else:
    print('Aluno Reprovado.')


