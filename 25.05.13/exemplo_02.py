import sys

try:
    intdividendo = int(input('Digite o dividendo: '))
    intdivisor = int(input('Digite o divisor: '))
    fltresultado = intdividendo / intdivisor
except ValueError:
    print('ERRO: Informe um valor que possa ser convertido em Inteiro.')
except ZeroDivisionError:
    print('ERRO: Não existe divisão por ZERO.')
except Exception as tipoExcecao:
    print(f'ERRO: {tipoExcecao}')
    print(f'ERRO: {sys.exc_info()}')
else:
    print(fltresultado)