'''Faça um programa que simule o jogo da forca. O programa terá uma constante chamada PALAVRA_CHAVE que armazenara 
a palavra a ser descoberta (o programador deverá atribuir uma string ao eu critério para essa constante). 

O programa deverá solicitar ao usuário as letras e à medida que as letras forem sendo digitadas o programa irá exibir se o usuário acertou ou não. 

O jogo deverá considerar maiúsculas e minúsculas iguais. O jogador poderá errar 6 vezes antes de ser enforcado.'''

# Definir a palavra chave.
palavra_chave = 'Asa Noturna'
palavra = palavra_chave.lower() # Assim letras maiúsculas e minúsculas são tratadas da mesma forma.

# Criar string do andamento do jogo.
progresso = ''

# Verifica a string 'palavra_chave', mostrando '_' para cada letra e espaço ' ' onde há espaço e inicializando o 'progresso' vazio.
for caractere in palavra_chave:
    if caractere == ' ':
        progresso = progresso + ' '
    else:
        progresso = progresso + '_' 

# Definir o contador da quantidade de erros.
erros = 0

# Criar string das letras que já foram usadas.
letras_usadas = ''

# Loop do jogo forca.
while '_' in progresso and erros < 6:
    print(f'palavra:{progresso}')
    print(f'\nLetras usadas:{letras_usadas}')
    print(f'Erros restantes:{6 - erros}, tente não errar mais que isso...')

# Solicitar uma letra ao jogador e criar condições.
    letra = input('Digite uma letra: ').lower()
    
    if len(letra) != 1: # Verificando se foi digitada apenas uma letra.
        print('Digite apenas uma letra por vez...')
        continue # 'continue' faz o programa voltar para o topo do laço e solicitar outra letra.

    if not letra.isalpha(): # Verificação com .isalpha() para saber se o caractere que foi digitado é algo do alfabeto.
        print('Digite apenas letras (sem números ou símbolos).')
        continue

    if letra in letras_usadas: # Verificando se a letra foi repetida.
        print('Você já utilizou essa letra, tente outra...')
        continue

    letras_usadas += letra # Registrando nova letra.

# Verificar se a letra pertence a palavra chave.
    if letra in palavra:
        progresso_novo = '' # String nova do progresso.
        for posicao in range(len(palavra_chave)): # posicao é o número da posição (índice) na string.
            if palavra[posicao] == letra: # [] vai acessar o caractere na posição da string, e verificar se é igual a letra dada pelo jogador.
                progresso_novo = progresso_novo + palavra_chave[posicao] # Mostra a letra igual a dada pelo jogador.
            else:
                progresso_novo = progresso_novo + progresso[posicao] # Continua com o que já tinha ( letra mostrada ou _ ou o espaço por ser palavra composta ).
        
        progresso = progresso_novo
        print('Ótima tentativa, acertou!')
    else:
        erros += 1 # Conta +1 nos erros.
        print('Errou!')

# Resultado: Jogador venceu ou perdeu na FORCA.
print('--- Resultado: ---')
if '_' in progresso:
    print(f'\nDERROTA: O Jogador foi enforcado!')
    print(f'A PALAVRA ERA: {palavra_chave}')
else:
    print(f'VItÓRIA: Você descobriu a palavra:{palavra_chave}')

print('\n--- Fim do jogo, obrigado pelo teste!"-" ---')













