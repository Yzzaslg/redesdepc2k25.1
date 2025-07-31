import os, sys

strDir = os.path.dirname(__file__)
try:
    arqEntrada = open(f'{strDir}\\produtos_informatica.csv', 'r', encoding='utf-8')
    linhas = arqEntrada.readlines()
except FileNotFoundError:
    sys.exit('\nERROR: Arquivo não existe...')
except Exception as erro:
   sys.exit(f'\nERROR: {erro}...')

produtos = [linha.strip().split(";") for linha in linhas[1:] if len(linha.strip().split(";")) == 5]
produtos = [[row[0], row[1], float(row[2]), float(row[3]), float(row[4])] for row in produtos]

empresa = input("Escolha a empresa para aplicar o desconto (A, B ou C): ").strip().upper()
desconto = float(input("Informe o percentual de desconto: "))

indices = {"A": 2, "B": 3, "C": 4}


idx = indices[empresa]
produtos_com_desconto = list(map(lambda p: p[:idx] + [round(p[idx] * (1 - desconto / 100), 2)] + p[idx+1:], produtos))

resultado = list(map(
    lambda p: [
        p[0], 
        p[1], 
        min(p[2:5]),  
        ["Empresa A", "Empresa B", "Empresa C"][p[2:5].index(min(p[2:5]))]  # Empresa com menor preço
    ],
    produtos_com_desconto
))

try:
    with open("RESULTADO_LICITACAO.csv", "w", encoding="utf-8") as file:
        file.write("Nome;Categoria;Menor Preço;Empresa\n")
        file.writelines([f"{r[0]};{r[1]};{r[2]};{r[3]}\n" for r in resultado])
    print("Arquivo RESULTADO_LICITACAO.CSV gerado com sucesso!")
except Exception as e:
    sys.exit(f"ERROR: ao escrever o arquivo: {e}")
