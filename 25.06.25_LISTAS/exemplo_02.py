'''
   Fazer um programa que:
   
      1) Solicite ao usuário um valor inteiro N positivo (valor máximo para N -> 100);
   
      2) Gere uma lista com N valores inteiros aleatórios entre 0 e 1.000 (inclusive)
         sem repetições;

      3) A partir da lista gerada, gere uma segunda uma lista com as raízes quadradas 
         dos valores da lista anterior;
'''
import sys, random, math

try:
# Solicitar o valor positivo ao usuário.
    intN = int(input('Informe um valor positivo ( entre 1 e 100 ): '))
    if intN <= 0 or intN > 100:
        sys.exit('Informe um valor positivo entre 1 e 100.')
except ValueError:
    sys.exit('\nERRO: Informe um valor inteiro válido...\n')
except Exception as erro:
    sys.exit(f'\nERRO: {erro}...\n')

else:
# Criar lista com tamanho determinado por N ( intN ) entre 0 e 1000.

    lstN = random.sample(range(0, 1001), intN) # random.sample (population = conjunto de valores possivel, k = quantos valores únicos) gera números aleatórios únicos, sem repetição.

    lstN.sort()

# Criar a lista as raízes quadradas dos valores anteriores.
    lstN_raiz = list()

    for N_raiz in lstN:
        if N_raiz >=0: # não existe raíz quadrada negativa.
            raizes = math.sqrt(N_raiz) # math.sqrt = calcula a raiz quadrada de um número.
            lstN_raiz.append(raizes)
    
    lstN_raiz.sort()

# Resultado:
print('--- Resultado ---')
print(f'\nLista original: {lstN}')
print(f'Lista com raízes quadradas: {lstN_raiz}')
print('\n--- Fim do programa, obrigado pelo teste!"-" ---')