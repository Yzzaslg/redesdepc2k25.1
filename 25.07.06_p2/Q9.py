'''Nesta questão, você implementará uma versão da cifra de Vigenère que utiliza todos os caracteres imprimíveis do teclado, incluindo letras maiúsculas e minúsculas, 
letras acentuadas, números, símbolos, e espaços em branco. Todos os caracteres, incluindo espaços e letras acentuadas, serão criptografados de acordo com a chave fornecida.


A chave de criptografia será formada pelos últimos 9 caracteres do texto de entrada (strTexto), mas esses últimos 9 caracteres também devem ser criptografados utilizando a 
cifra de Vigenère antes de serem usados como chave. Ou seja, você deve criptografar o texto, gerar a chave a partir dos 9 últimos caracteres do texto criptografado, e então 
aplicar essa chave na cifra do texto completo.'''