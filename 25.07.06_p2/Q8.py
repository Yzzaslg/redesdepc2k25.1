'''Um robô pode se mover em oito sentidos em um plano cartesiano: U (cima); D (baixo); R (direita); L (esquerda); O (noroeste/cima-esquerda); 
N (nordeste/cima-direita); E (sudeste/baixo-direita) e W (sudoeste/baixo-esquerda).

Faça um programa que:

Solicite ao usuário a posição inicial do robô (suas coordenadas X e Y);
Solicite ao usuário uma string. Letras maiúsculas e minúsculas são indistintas e aquelas informadas que estejam fora das estabelecidas (U, D, R, L, O, N, E e W) 
devem ser ignoradas;
Com base em cada letra válida (U, D, R, L, O, N, E e W), o robô deverá se deslocar 1 (uma) unidade em cada eixo (X e Y) por vez em função da direção;

Ao final, indique:

A posição inicial do robô (coordenadas X e Y);
A posição final do robô (coordenadas X e Y);
Quantos movimentos válidos ele executou;
Quais foram os movimentos válidos que ele executou;
Em que quadrante ele iniciou (posição inicial de X e Y) e;
Em que quadrante ele terminou (posição final de X e Y).'''

import sys

# Solicitar as posições iniciais ao usuário
try:
    x_i = int(input('Dgite um valor para a posição X inicial: '))
    y_i = int(input('Dgite um valor para a posição Y inicial: '))
except ValueError:
    sys.exit('Valor inválido, por favor digite valores inteiros para X e Y...')
except Exception as e:
    sys.exit(f'ERRO: {e}')

# String de comandos
comandos = input('Digite os comandos de movimentos do robô (U, D, R, L, O, N, E e W) : ')
comandos = comandos.upper() # Converter para maiúsculo como padrão.
if comandos.strip() == '': # .strip elimina os espaços da esquerda e direita nas strings, caso o usuário digite apenas espaço e der enter, strip retorna uma string vazia inválida para os movimentos.
    sys.exit('Nenhum comando foi digitado, o robô não vai se mover...')

# Variáveis dos moviementos
x = x_i
y = y_i
movimentos_validos = ''
movimentos_invalidos = ''
movimentos = 0

# Loop da sequência de movimentos
for letra in comandos:
# Mapeamento das direções
# As letras U/D mexem só no eixo Y, L/R mexem só no eixo X,
# e as diagonais (N, O, E, W) são combinação dos dois.
    if letra == 'U': # Cima
        x = x + 0
        y = y + 1
        movimentos_validos = movimentos_validos + letra
        movimentos = movimentos + 1
    elif letra == 'D': # Baixo
        x += 0
        y += -1
        movimentos_validos += letra
        movimentos += 1
    elif letra == 'R': # Direita
        x += 1
        y += 0
        movimentos_validos += letra
        movimentos += 1        
    elif letra == 'L': # Esquerda
        x += -1
        y += 0
        movimentos_validos += letra
        movimentos += 1
    elif letra == 'N': # Cima-direita/nordeste
        x += 1
        y += 1
        movimentos_validos += letra
        movimentos += 1
    elif letra == 'O': # Cima-esquerda/noroeste 
        x += -1
        y += 1
        movimentos_validos += letra
        movimentos += 1
    elif letra == 'E': # Baixo-direita/sudeste
        x += 1
        y +=-1
        movimentos_validos += letra
        movimentos += 1
    elif letra == 'W': # Baixo-esquerda/sudoeste
        x += -1
        y += -1
        movimentos_validos += letra
        movimentos += 1
    else:
        movimentos_invalidos += letra # Vai retornar as letras inválidas dos movimentos.

# Registro dos quadrantes
# Qudrantes iniciais:
if x_i > 0 and y_i > 0:
    quadrante_i = 'Quadrante I'
elif x_i < 0 and y_i > 0:
    quadrante_i = 'Quadrante II'
elif x_i < 0 and y_i < 0:
    quadrante_i = 'Quadrante III'
elif x_i > 0 and y_i < 0:
    quadrante_i = 'Quadrante IV'
elif x_i == 0 and y_i == 0:
    quadrante_i = 'Origem'
elif x_i == 0:
    quadrante_i = 'No eixo Y'
elif y_i == 0:
    quadrante_i = 'No eixo X'

# Quadrantes finais:
if x > 0 and y > 0:
    quadrante = 'Quadrante I'
elif x < 0 and y > 0:
    quadrante = 'Quadrante II'
elif x < 0 and y < 0:
    quadrante = 'Quadrante III'
elif x > 0 and y < 0:
    quadrante = 'Quadrante IV'
elif x == 0 and y == 0:
    quadrante = 'Origem'
elif x == 0:
    quadrante = 'No eixo Y'
elif y == 0:
    quadrante = 'No eixo X'

# Resultados.
print('--- Resultados: ---')
print(f'\nPosição inicial do robô: ({x_i},{y_i}) ')
print(f'Posição final do robô: ({x},{y})')
print(f'Quantidade de movimentos efetuados: {movimentos}')
print(f'Movimentos efetuados: {movimentos_validos}')
print(f'Letras inválidas para os movimentos:{movimentos_invalidos}')
print(f'Quadrante inicial: {quadrante_i}')
print(f'Quadrante final: {quadrante}')
print('\n--- Fim do programa, obrigado pelo teste!"-" ---')