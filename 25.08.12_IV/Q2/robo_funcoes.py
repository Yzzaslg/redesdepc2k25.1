def quadrantes(posicaoXY: tuple) -> tuple:
    x, y = posicaoXY
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
    
    return ((x,y), quadrante)

def movimenta(posicaoXY: tuple, comandos: str) -> tuple:
    x, y = posicaoXY
    movimentos_validos = ''
    movimentos_invalidos = ''
    movimentos = 0

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

    return (posicaoXY, movimentos_validos, movimentos_invalidos, movimentos, (x, y))