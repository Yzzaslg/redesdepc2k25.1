'''Na definição da Wikipédia, números triangulares são aqueles que representam o total de pontos que formam triângulos equiláteros em um plano 
(veja a definição detalhada em https://pt.wikipedia.org/wiki/Número_triangular).

Faça um programa que solicite ao usuário um número inteiro positivo e informe se ele é (ou não) triangular, de acordo com a definição.
'''
import sys

# Solicitar o número ao usuário.
try:
    num = int(input('Informe um número inteiro positivo: '))
    if num <= 0:
        sys.exit('O Número deve ser positivo!')
except ValueError:
    sys.exit('Informe apenas valores reais para o número.')
except Exception as e:
    sys.exit(f'ERRO: {e}')

# 'n' vai começar em 1.
else:
    n = 1

while n * ( n + 1 ) / 2 <= num:
# Definição do número triangular: Tn = 1+2+3+⋯+n = n(n+1)/2.    
    T = n * ( n + 1 ) / 2
    print(f'T ={T}')
    if T == num:
        print('Achou! O número inserido é triangular.')
        break # break vai parar o programa caso número dado pelo usuário seja igual ao triangular ( num == T ).
    n = n + 1 # caso o número dado não seja igual ou maior ao triangular, o programa irá rodar novamente adicionando +1 a variável 'n'.
else:
    print('Puts! O número informado não é triangular.')

print('\n--- Fim do programa, obrigado pelo teste!"-" ---')