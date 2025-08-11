'''Com base no trecho de código fornecido pede-se que seja implementado um programa que siga as 
instruções abaixo (não esqueça de copiar o trecho do código fornecido para dentro do seu programa):
a. Solicite ao usuário o ano desejado (o ano informado não pode ser superior ao ano atual, para isso 
deve-se usar as funções/métodos da biblioteca DATETIME para obter/validar o ano atual;
b. Com base no ano informado deve-se (a) requisitar na WEB (conforme código disponibilizado) caso 
seja informado o ano atual ou (b) carregar o dicionário do arquivo do CartolaFC relativo ao ano 
informado caso seja informado anos anteriores ao ano atual (os arquivos encontram-se disponíveis 
no repositório desta atividade);
c. Uma vez que a variável dictCartola esteja com os dados do CartolaFC, o programa deverá solicitar 
o esquema tático desejado. Os esquemas táticos possíveis são: 3-4-3, 3-5-2, 4-3-3, 4-4-2, 4-5-1, 
5-3-2 ou 5-4-1;
d. Para cada esquema tático, deve-se selecionar a seguinte quantidade de jogadores por posição;
e. Independente do esquema, todos terão de ter 1 goleiro e 1 técnico;
f. A escolha dos atletas de cada posição será através dos atletas que tiverem a maior pontuação 
(média de pontos x quantidade de partidas) em cada posição (zagueiro, lateral, meia, atacante, 
goleiro, técnico). Atente para a quantidade de atletas em cada posição em função do esquema tático 
selecionado;
g. Gerar um dicionário no formato k:v onde a chave k será o valor da chave será o id do atleta e o 
valor v será um dicionário no formato k:v onde as chaves ficam a critério de vocês e os valores 
serão: o id do atleta, o nome do atleta, o apelido do atleta, a URL da foto do atleta, o nome do 
clube, o escudo do clube, o id da posição, o nome da posição e a pontuação do atleta (média de pontos 
x quantidade de partidas). Esse dicionário deverá ser salvo no formato JSON no mesmo diretório/pasta 
do programa;
ATENÇÃO: Na URL da foto do jogador nem sempre tem a string _220x220_, as vezes vem a string _FORMATO_ 
ou _FORMATO. Logo, quando aparecer a string _FORMATO_ ela deve ser substituída pela string _220x220_ 
e quando aparecer a string _FORMATO ela deve ser substituída pela string _220x220.
h. O programa deverá exibir, após todo o processamento necessário, a seleção do Cartola FC com as 
seguintes informações: o nome da posição (obedecer a seguinte ordem: goleiro, zagueiro, lateral, 
meia, atacante, técnico), o nome do atleta e seu apelido, o nome do time que o atleta joga e a 
pontuação (média x quantidade de partidas) do atleta;
i. Lembre-se de tratar as devidas exceções no programa (conversões de valores, requisições na WEB, 
manipulação de arquivos, ...). Elas são obrigatórias.
'''
from datetime import datetime
from Q2_funçoes import dicionario_cartola, escolher_escalacao_e_quantidades, definir_selecao, salvar_exibir_selecao

# Solicitar ano ao usuário.
ano_atual = datetime.now().year

while True:
    try:
        ano = int(input(f"Informe o ano desejado (de 2021 até {ano_atual}): "))
        if 2021 <= ano <= ano_atual:
            break
        else:
            print(f"ERR0: O ano informado é inválido, informe entre 2021 e {ano_atual}.")
    except ValueError:
        print('Digite um número inteiro para o ano.')
    except Exception as e:
        print(f'ERR0: {e}')

dicCartola = dicionario_cartola(ano, ano_atual)

# Definir escalação e quantidades de atletas
escalacoes = ['3-4-3', '3-5-2', '4-3-3', '4-4-2', '4-5-1', '5-3-2', '5-4-1'] # exibir as escalações disponíveis do cartolaFC.
print('Escolha uma das escalações disponíveis:')
for i, esc in enumerate(escalacoes, start=1):
    print(f'{i} - {esc}')

# solicitar a escalação desejada.
while True:
    try:
        escalacao = int(input('Defina uma escalação ( 1-7 ): '))
        if 1 <= escalacao <= 7:
            break
        else:
            print(f'ERR0: Escalação inválida. Escolha uma das opções: {escalacoes}')
    except ValueError:
        print('ERR0: Por favor, digite um número válido.')
    except Exception as e:
        print(f'ERR0: {e}')

escalacao, quantidades_atletas = escolher_escalacao_e_quantidades(escalacoes, escalacao)

# Definir seleção de atletas ( time final do Cartola FC com os melores jogadores por posição ).
selecao_atletas, ordem = definir_selecao(dicCartola, quantidades_atletas)

# Salvar e exibir resultados da seleção.
salvar_exibir_selecao(selecao_atletas, ano, ordem)

print('\n--- Fim do programa, obrigado pelo teste!"-" ---')