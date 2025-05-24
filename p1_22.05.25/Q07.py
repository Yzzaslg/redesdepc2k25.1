'''Com base nas novas regras da Previdência Social estabelecidas pela Emenda Constitucional nº 103/2019, desenvolva um programa em Python que solicite oa usuário as seguintes informações de uma pessoa::

Sexo da pessoa (masculino/feminino);
Data de nascimento da pessoa (no formato DD/MM/AAAA);
Data de início da contribuição previdenciária da pessoa (no formato DD/MM/AAAA).

O programa deve então calcular e exibir a data em que a pessoa poderá se aposentar, considerando as seguintes regras de transição, com os pedágios aplicáveis para cada caso:


Aposentadoria por Idade:
Homens: podem se aposentar aos 65 anos, desde que tenham pelo menos 15 anos de contribuição.;
Mulheres: podem se aposentar aos 62 anos, desde que tenham pelo menos 15 anos de contribuição;
Para a aposentadoria por idade, não há pedágio adicional.'''

import sys
import datetime # Usei datetime pois converte as datas em objetos para que eu pudesse usar em cálculos.

# Dados do usuário
sexo = input('Informe seu sexo (feminino/masculino): ')
try:
    dia_nasc = int(input('Informe seu dia de nascimento: '))
    mes_nasc = int(input('Informe seu mês de nascimento: '))
    ano_nasc = int(input('Informe seu ano de nascimento: '))
    dia_ini_contri = int(input('Informe o dia de inicio da sua contribuição previdenciária: '))
    mes_ini_contri = int(input('Informe o mes de inicio da sua contribuição previdenciária: '))
    ano_ini_contri = int(input('Informe o ano de inicio da sua contribuição previdenciária: '))

    print(f'Sexo do usuário:{sexo}')
    print(f'Data de nascimento do usuário:{dia_nasc:02d}/{mes_nasc:02d}/{ano_nasc:02d}.')
    print(f'Data de inicio da contribuição previdenciária:{dia_ini_contri:02d}/{mes_ini_contri:02d}/{ano_ini_contri:02d}.')

except ValueError:
    sys.exit('Digite apenas valores reais.')
except Exception as excecao:
    print(f'ERRO> {excecao}')

# converter com datetime em um objeto as datas.
data_nasc = datetime.datetime(ano_nasc, mes_nasc, dia_nasc)
data_contri = datetime.datetime(ano_ini_contri, mes_ini_contri, dia_ini_contri)

# Registrar a data e hora atuais na variável objeto.
hoje = datetime.datetime.today() # vai servir para comparar com as próximas datas.

# Calcular as datas
idade = hoje.year - data_nasc.year # verifica se o aniversário já aconteceu no ano atual, se sim ()<() = 0, se não, ()<() = 1.
if ((hoje.month < data_nasc.month) or ( hoje.month == data_nasc.month and hoje.day < data_nasc.day)):
    idade = idade - 1
tempo_contri = hoje.year - data_contri.year
if ((hoje.month < data_contri.month) or ( hoje.month == data_contri.month and hoje.day < data_contri.day)):
    tempo_contri = tempo_contri - 1

# Condição da idade minimia masculina (65 anos ) e feminina (62 anos ).
idade_minima_feminino = 62 # 62 anos
idade_minima_masculino = 65 # 65 anos
tempo_minimo_contri = 15 # 15 anos

# Condição pelo tempo de contribuição masculina ( 35 anos ) e feminina ( 30 anos ).
tempo_minimo_contri_masc = 35
tempo_minimo_contri_femi = 30
ano_da_reforma = 2019

# Idade minima de acordo com sexo do usuário.
sexo_lower = sexo.lower()
if sexo_lower == 'feminino':
    idade_minima = idade_minima_feminino
    tempo_minimo = tempo_minimo_contri_femi
elif sexo_lower == 'masculino':
    idade_minima = idade_minima_masculino
    tempo_minimo = tempo_minimo_contri_masc
else:
    sys.exit('Informe o sexo do usuário apenas como feminino ou masculino.')
    idade_minima = 0

# Verificação de aposentadoria por idade minima.
if idade >= idade_minima and tempo_contri >= tempo_minimo_contri:
    print('Parabéns, você já tem idade o suficiente para se aposentar.')
else:
    anos_que_faltam_idade = idade_minima - idade
    if anos_que_faltam_idade < 0:
        anos_que_faltam_idade = 0

    anos_que_faltam_contri = tempo_minimo_contri - tempo_contri
    if anos_que_faltam_contri < 0:
        anos_que_faltam_contri = 0
    
    if anos_que_faltam_idade > anos_que_faltam_contri:
        anos_que_faltam = anos_que_faltam_idade
    else:
        anos_que_faltam = anos_que_faltam_contri

# Data aposentadoria por idade.
data_aposentadoria_idade = hoje + datetime.timedelta( days=anos_que_faltam * 365 ) # timedelta = representa uma diferença entre duas datas, ( * 365 ) para converter em dias os anos que faltam.
dia_aposentadoria = data_aposentadoria_idade.day
mes_aposentadoria = data_aposentadoria_idade.month
ano_aposentadoria = data_aposentadoria_idade.year
print(f'Sua aposentadoria por idade poderá acontecer em:{dia_aposentadoria:02d}/{mes_aposentadoria:02d}/{ano_aposentadoria:02d}.')

# Verificação de aposentadoria por tempo de contribuição com pedágio.
if data_contri.year < ano_da_reforma:
    anos_que_faltam_contri = tempo_minimo_contri - tempo_contri
    if anos_que_faltam_contri < 0:
        anos_que_faltam_contri = 0

# Calculo pedágio de 50%.
pedagio = int( anos_que_faltam_contri * 0.5 ) # pelo que li, apenas o pedágio de 50% é aplicado na prática e foi pedido na questão.
total_que_falta_contri = anos_que_faltam_contri + pedagio

# Data aposentadoria por pedágio.
data_aposentadoria_pedagio = hoje + datetime.timedelta( days = int( total_que_falta_contri*365 ))
dia_pedagio = data_aposentadoria_pedagio.day
mes_pedagio = data_aposentadoria_pedagio.month
ano_pegadio = data_aposentadoria_pedagio.year
print(f'Sua aposentadoria por tempo de contribuição com pedágio poderá acontecer em:{dia_pedagio:02d}/{mes_pedagio:02d}/{ano_pegadio:02d}.')