# Fazer um programa para solicitar o valor de uma venda e
# o percentual da comissão e exibir o valor da comissão

valor_venda = float(input('Digite o valor da venda (R$): '))
percentual = float(input('Informe a comissão (%)......'))

comissão = valor_venda * percentual / 100

print(f'O valor da comissão é R$ {comissão:.2f}')