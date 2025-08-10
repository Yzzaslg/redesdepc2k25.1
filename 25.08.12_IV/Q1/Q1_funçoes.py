import sys
from datetime import datetime

__all__ = ['listar_moedas', 'calculo_medias_mensais']

# ----- FUNÇÃO 1 ----- LISTAR MOEDAS.
def listar_moedas(dicMoedas):
    try:
        if 'value' not in dicMoedas:
            sys.exit('ERR0: "value" não existe no arquivo.')
        else:
            lstMoedas = [moeda['simbolo'] for moeda in dicMoedas['value']]
            for moeda in dicMoedas['value']:
                print(moeda['simbolo'], '/', moeda['nomeFormatado'])
    except Exception:
        sys.exit('ERR0: Não é possivel obter lista de moedas disponíveis.')
    return lstMoedas

# ----- FUNÇÃO 2 ----- VALIDAÇÃO DOS MESESCALCULAR AS MÉDIAS.
def calculo_medias_mensais(dicCotacoes):
    Meses = {
        1: "Janeiro", 2: "Fevereiro", 3: "Março", 4: "Abril", 5: "Maio", 6: "Junho",
        7: "Julho", 8: "Agosto", 9: "Setembro", 10: "Outubro", 11: "Novembro", 12: "Dezembro"
    }

# Verificação da chave 'value'.
    if 'value' not in dicCotacoes:
        sys.exit('ERR0: Formato inválido, chave: "value" não existe no arquivo.')

# Valida se a lista de cotações não está vazia.
    cotacoes = dicCotacoes['value']
    if len(cotacoes) == 0:
        sys.exit('ERR0: Nenhuma cotação encontrada para o ano verificado.')

    resultado_cotacoes = {} # dicionário vazio

# Verificação das cotações ( chaves necessárias ).
    for cot in cotacoes:
        if 'dataHoraCotacao' not in cot or 'cotacaoCompra' not in cot or 'cotacaoVenda' not in cot:
            sys.exit('ERR0: Campos necessários não encontrados.')
        
# Selecionar mês desejado.
        try:
            data = datetime.fromisoformat(cot['dataHoraCotacao']) # Converte a string em um objeto.
            mes = data.month
        except Exception:
            sys.exit(f"ERR0: Data inválida: {cot['dataHoraCotacao']}")
    
        mes_nome = Meses[mes] # obter o nome do mês do dicionário meses.

# Se o mês não existir na variavel: resultado_cotacoes, cria a estrutura.
        if mes_nome not in resultado_cotacoes:
            resultado_cotacoes[mes_nome] = {"mediaCompra": [],"mediaVenda": []}

    # Adiciona os valores às listas
        resultado_cotacoes[mes_nome]["mediaCompra"].append(cot["cotacaoCompra"])
        resultado_cotacoes[mes_nome]["mediaVenda"].append(cot["cotacaoVenda"])

# Calcular as médias mensais.
    for mes_nome in resultado_cotacoes:
        medias_compra = resultado_cotacoes[mes_nome]["mediaCompra"]
        medias_venda = resultado_cotacoes[mes_nome]["mediaVenda"]

        resultado_cotacoes[mes_nome]["mediaCompra"] = round(sum(medias_compra) / len(medias_compra), 3)
        resultado_cotacoes[mes_nome]["mediaVenda"] = round(sum(medias_venda) / len(medias_venda), 3)

    return resultado_cotacoes # retorna o dicionário resultado_cotacoes com os valores.