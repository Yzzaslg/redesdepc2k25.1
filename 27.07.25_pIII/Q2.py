'''Fazer um programa para gerar automaticamente uma lista de dimensão de n elementos (n deverá ser solicitado ao usuário, positivo e entre 7 e 60, inclusive), 
cada elemento dessa lista será um número aleatório entre 1 e 60 (inclusive) sem repetição. Após a lista ser gerada, as seguintes operações deverão ser implementadas:

i. Deverá ser criada uma segunda lista com todas as combinações possíveis de 6 dezenas. Cada combinação deverá ser uma sub-lista. Cada combinação deverá estar ordenada do 
menor número para o maior;
ii. A lista de números escolhidos deverá ser salva em um arquivo chamado NUMEROS_ESCOLHIDOS.TXT (salvar no mesmo diretório/pasta em que o programa está salvo). 
Nesse arquivo os números deverão estar em apenas 1 linha. Utilize espaço em branco para separar os valores na linha;
iii. A lista de combinações deverá ser salva em um arquivo chamado COMBINACOES.CSV (salvar no mesmo diretório/pasta em que o programa está salvo). 
Nesse arquivo cada combinação deverá estar em 1 linha. Utilize ponto e vírgula para separar os valores na linha;
iv. No final deverão ser exibidos na tela quantas combinações foram geradas, e quais as probabilidades de se acertar a sena, a quina e a quadra.'''

import sys, random

# Solicitar quantidade de elementos, dado por n.
try:
    n = int(input('Informe um número positivo e entre 7 e 60: '))
    if n < 7 or n > 60:
        sys.exit('ERR0: Informe um número positivo válido.')
except ValueError:
    sys.exit('ERR0: Informe apenas valores inteiros.')
except Exception as e:
    sys.exit(f'ERR0: {e}')

# Gerar números aleatórios da lista entre 1 e 60.
numeros = sorted(random.sample(range(1, 61), n )) # random.sample (population = conjunto de valores possivel, n_elementos = quantos valores únicos) gera números aleatórios únicos, sem repetição.

# Combinações de 6 dezenas possíveis.
combinacoes = []
for i in range(n - 5):
    for j in range(i + 1, n - 4):
        for k in range(j + 1, n - 3):
            for l in range(k + 1, n - 2):
                for m in range(l + 1, n - 1):
                    for o in range(m + 1, n):
                        posicoes = [i, j, k, l, m, o]
                        combinacoes.append([numeros[z] for z in posicoes])

# Salvar lista de números em NUMEROS_ESCOLHIDOS.TXT.
with open("NUMEROS_ESCOLHIDOS.TXT", "w") as arquivo: # with - garante que o arquivo será fechado, open - abre o arquivo ou cria e w - modo da escrita.
    for i in range(len(numeros)):
        arquivo.write(str(numeros[i])) # write() escreve o conteúdo.
        if i != n - 1: # se a posição de i for diferente da última posição da lista.
            arquivo.write(" ") # será adicionado espaço pós a posição ( número ).

# Salvar lista de combinações em COMBINACOES.CSV.
with open("COMBINACOES.CSV", "w") as arquivo:
    for combi in combinacoes:
        for i in range(len(combi)):
            arquivo.write(str(combi[i]))
            if i != len(combi) - 1:
                arquivo.write(";")
        arquivo.write("\n")

# Resultado total das combinações.
total = 0
for _ in combinacoes:
    total += 1
print('\nTotal de combinações geradas:', total)

# Cálculo das probabilidades.
# fórmula da combinação: C(n,k)= n! / k!⋅(n−k)!; Sena = 6 números, quina = 5 números e quadra = 4 números. 
fato_n = 1 # fatorial de n!.
for i in range (2, n + 1):
    fato_n *= i

fato_6 = 1 # fatorial de 6!.
for i in range(2, 7):
    fato_6 *= i

fato_n_6 = 1 # fatorial de ( n - 6 )!.
for i in range(2,n - 6 + 1):
    fato_n_6 *= i

fato_5 = 1 # fatorial de 5!
for i in range(2, 6):
    fato_5 *= i

fato_n_5 = 1 # fatorial de ( n - 5 )!.
for i in range(2, n - 5 + 1):
    fato_n_5 *= i

fato_4 = 1 # fatorial de 4!.
for i in range(2, 5):
    fato_4 *= i

fato_n_4 = 1 # fatorial de ( n - 4 )!.
for i in range(2, n - 4 + 1):
    fato_n_4 *= i


# Combinação de n de 6 em 6.
combi_n_6 = fato_n // ( fato_6 * fato_n_6 ) # Sena

# Combinação de n de 5 em 5.
combi_n_5 = fato_n // ( fato_5 * fato_n_5 ) # Quina

# Combinação de n de 4 em 4.
combi_n_4 = fato_n // ( fato_4 * fato_n_4 ) # Quadra

# Resultado das probabilidades.
print('\nProbabilidades: ')
print(f"\nAcertar a SENA: 1 em {combi_n_6}") # só há uma chance de acertar a SENA.
print(f"Acertar a QUINA: 1 em {combi_n_5 // 6}") # 6 subconjuntos de 5 em cada combinação de 6.
print(f"Acertar a QUADRA: 1 em {combi_n_4 // 15}") # 15 subconjuntos de 4 em cada combinação de 6.

print('\n--- Fim do programa, obrigado pelo teste!"-" ---')










 
