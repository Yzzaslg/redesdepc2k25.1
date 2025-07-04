'''
   Fazer um programa que:
   
      1) Solicite ao usuário um valor inteiro N positivo (valor máximo para N -> 100);

      2) Gere uma lista com N valores inteiros aleatórios entre -100 e +100;
   
      3) A partir da lista gerada, gere uma segunda uma lista apenas com os 
         números pares da lista;
'''
import sys, random

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
# Criar lista com tamanho determinado por N ( intN ) entre -100 e +100.    
    lstN = list()

    for _ in range (intN):
        lstN.append(random.randint(-100, 100))

    lstN.sort()

# Criar a lista com números pares.
    lstN_par = list()    

    for Npares in lstN:
        if Npares % 2 == 0:
            lstN_par.append(Npares)

    lstN_par.sort()

# Resultado.
print('--- Resultado ---')
print(f'\nLista original: {lstN}')
print(f'Lista com números pares: {lstN_par}')
print('\n--- Fim do programa, obrigado pelo teste!"-" ---')



 


    
    
    
