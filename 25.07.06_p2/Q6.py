'''Tomando por base a definição de Constante de Kaprekar (https://pt.wikipedia.org/wiki/Constante_de_Kaprekar) faça um programa que receba um inteiro positivo de no máximo 4 dígitos e exiba em quantas iterações esse número converge para a Constante de Kaprekar. Exiba as iterações também.

Para que um número de 4 dígitos não convirja para 6174, a restrição a ser considerada é a seguinte: número tiver todos os seus dígitos iguais, como 1111, 2222, 3333, etc., o processo de Kaprekar não funcionará, porque a diferença entre o número maior (formado pelos dígitos em ordem decrescente) e o menor (formado pelos dígitos em ordem crescente) será sempre zero.

Por exemplo:

para n = 3524, o programa deverá exibir a seguinte saída:

Iterações:
5432 – 2345 = 3087
8730 – 0378 = 8352
8532 – 2358 = 6174

Nº de Iterações: 3'''