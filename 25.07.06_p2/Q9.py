'''Nesta questão, você implementará uma versão da cifra de Vigenère que utiliza todos os caracteres imprimíveis do teclado, incluindo letras maiúsculas e minúsculas, 
letras acentuadas, números, símbolos, e espaços em branco. Todos os caracteres, incluindo espaços e letras acentuadas, serão criptografados de acordo com a chave fornecida.


A chave de criptografia será formada pelos últimos 9 caracteres do texto de entrada (strTexto), mas esses últimos 9 caracteres também devem ser criptografados utilizando a 
cifra de Vigenère antes de serem usados como chave. Ou seja, você deve criptografar o texto, gerar a chave a partir dos 9 últimos caracteres do texto criptografado, e então 
aplicar essa chave na cifra do texto completo.'''

# Definir a string tabela de caracteres
strCaracteres = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyzáàâãäåçéèêíìîóòôõöúùûüÁÀÂÃÄÅÇÉÈÊÍÌÎÓÒÔÕÖÚÙÛÜ0123456789 !"#$%&\'()*+,-./:;<=>?@[\\]^_{|}~'

# Definir a string texto
strtexto = 'Eu acredito que há um herói em todos nós, que nos mantém honestos, nos dá força, nos torna nobres, e finalmente nos permite morrer com orgulho, mesmo que às vezes ' \
'tenhamos que ser firmes e abrir mão daquilo que mais queremos, até mesmo nossos sonhos. O Homem-Aranha fez isso por Henry e ele se pergunta para onde ele foi. Ele precisa dele.'

# Criptografar o texto completo usando a cifra de Vigenère ( método de criptografia que usa uma palavra-chave ) com todos os caracteres imprimíveis.
# Criptografar o texto 'strtexto' com uma chave temporária
chave_random = '!UND3RR45ED!'
texto_random = ''
# Loop para criptografar com chave temporária
for posicao, caractere in enumerate(strtexto): # enumerate() percorre toda a string e retorna cada elemento junto com sua posição ( índice )
    posic_texto = strCaracteres.index(caractere) # idenx() procura a posição ( índice ) de um elemento dentro de uma sequência e retorna em número ( seu índice )
    posic_chave = strCaracteres.index(chave_random[posicao % len(chave_random)]) # Pegar o caractere da chave que corresponde à posição atual
    posic_nova = (posic_texto + posic_chave) % len(strCaracteres) # deslocamento: posição no texto + posição na chave, caso deslocamento ultrapassar tabela de caractres, % faz voltar para o inicio da posição na tabela por diante
    texto_random += strCaracteres[posic_nova] # Pega o caractere que corresponde a posição e acumula o resultado no texto temporário

# Criar a chave final com os últimos 9 caracteres criptografados
strchave = texto_random[-9:]

# Criptografar ( cifrar ) o texto original 'strtexto' com a chave final 'strchave' e gerar o texto criptografado.
cripto_texto = ''
for posicao, caractere in enumerate(strtexto):
    posic_texto = strCaracteres.index(caractere)
    posic_chave = strCaracteres.index(strchave[posicao % len(strchave)])
    posic_nova = (posic_texto + posic_chave) % len(strCaracteres)
    cripto_texto += strCaracteres[posic_nova]

# Descriptografar ( decifrar ) o texto criptografado 'cifra_texto' para retornar o original
descripto_texto = ''
for posicao, caractere in enumerate(cripto_texto):
    posic_texto = strCaracteres.index(caractere)
    posic_chave = strCaracteres.index(strchave[posicao % len(strchave)])
    posic_nova = (posic_texto - posic_chave) % len(strCaracteres) # Subtrai a posição da chave para desfazer o deslocamento aplicado na criptografia
    descripto_texto += strCaracteres[posic_nova]

# Resultados
print('--- Resultados: ---')
print(f'\nTexto original: {strtexto}')
print(f'\nTexto Criptografado (aleatório): {texto_random}')
print(f'\nTexto Criptografado: {cripto_texto}')
print(f'\nTexto Descriptografado: {descripto_texto}')
print('\n--- Fim do programa, obrigado pelo teste!"-" ---')