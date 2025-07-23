# Faça um programa que solicite ao usuário um valor decimal positivo 
# (esse valor corresponde ao valor de um saque em um terminal de caixa eletrônico) 
# e que calcule a quantidade de cédulas de R$ 100,00, R$ 50,00, R$ 20,00, R$ 10,00, R$ 5,00 e R$ 2,00 
# e de moedas de R$ 1,00, R$ 0,50, R$ 0,25, R$ 0,10, R$ 0,05 e R$ 0,01.

import sys

# Solicitando o valor do saque:
try:
    valor = float(input('Digite o valor referente ao saque no caixa eletrônico (positivo):R$ '))
    if valor < 0: # valor tem que ser positivo.
        sys.exit('Informe um valor de saque positivo')
    if round(valor * 100) != valor * 100: # round verifica que o valor não pode ter mais de duas casas decimais e != ( diferente de ).
         sys.exit('ERRO: O valor deve ter no máximo duas casas decimais.')


# Convertendo o valor para centavos ( facilita no cálculo )
    valorcent = int(round(valor * 100))
except ValueError:
        sys.exit('ERRO: Informe um valor que possa ser convertido em inteiro')
except Exception as excecao:
    print(f'ERRO: {excecao}')
    
# Informando quantidade de cédulas:
v100 = valorcent // 10000
valorcent %= 10000

v50 = valorcent // 5000
valorcent %= 5000

v20 = valorcent // 2000
valorcent %= 2000

v10 = valorcent // 1000
valorcent %= 1000

v5 = valorcent // 500
valorcent %= 500

v2 = valorcent // 200
valorcent %= 200

# Informando quantidade de moedas:
v1 = valorcent // 100
valorcent %= 100

v050 = valorcent // 50
valorcent %= 50

v025 = valorcent // 25
valorcent %= 25

v010 = valorcent // 10
valorcent %= 10

v005 = valorcent // 5
valorcent %= 5 

v001 = valorcent // 1
valorcent %= 1

# Quantidade de cédulas:
print(f'A quantidade de cédulas é: ') 
print(f'R$ 100.00: {v100} + R$ 50.00: {v50} + R$ 20.00: {v20} + R$ 10.00: {v10} + R$ 5.00: {v5} + R$ 2.00: {v2}')

# Quantidade de moedas:
print(f'A quantidade de moedas é: ')
print(f'R$ 1.00: {v1} + R$ 0.50: {v050} + R$ 0.25: {v025} + R$ 0.10: {v010} + R$ 0.05: {v005} + R$ 0.01: {v001}')