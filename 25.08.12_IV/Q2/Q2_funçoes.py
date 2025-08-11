import sys, requests, json
from datetime import datetime

def dados_cartola():
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

    if ano == ano_atual:
    # usar dados da api
        print('Requisitando dados da API para o ano atual...')
        strURLCartola = 'https://api.cartolafc.globo.com/atletas/mercado'
        try:    
            dicCartola = requests.get(strURLCartola).json()
        except requests.RequestException as e:
            sys.exit(f"ERR0: Falha na requisição à API: {e}")

    else:
    # carregar dicionário do arquivo de acordo com o ano.
        try:
            with open(f'cartola_{ano}.json', 'r', encoding='utf-8') as arquivo:
                dicCartola = json.load(arquivo)
        except FileNotFoundError:
            sys.exit(f"ERR0: Arquivo cartola_{ano}.json não encontrado.")
        except json.JSONDecodeError:
            sys.exit("ERR0: Erro ao decodificar o JSON do arquivo.")

    return ano, ano_atual, dicCartola

def escolher_escalacao_e_quantidades():
    # exibir as escalações disponíveis do cartolaFC.
    escalacoes = ['3-4-3', '3-5-2', '4-3-3', '4-4-2', '4-5-1', '5-3-2', '5-4-1']
    
    quantidades_escalacao = {
        '3-4-3': {'goleiro': 1, 'zagueiro': 3, 'lateral': 2, 'meia': 4, 'atacante': 3, 'tecnico': 1},
        '3-5-2': {'goleiro': 1, 'zagueiro': 3, 'lateral': 2, 'meia': 5, 'atacante': 2, 'tecnico': 1},
        '4-3-3': {'goleiro': 1, 'zagueiro': 4, 'lateral': 2, 'meia': 3, 'atacante': 3, 'tecnico': 1},
        '4-4-2': {'goleiro': 1, 'zagueiro': 4, 'lateral': 2, 'meia': 4, 'atacante': 2, 'tecnico': 1},
        '4-5-1': {'goleiro': 1, 'zagueiro': 4, 'lateral': 2, 'meia': 5, 'atacante': 1, 'tecnico': 1},
        '5-3-2': {'goleiro': 1, 'zagueiro': 5, 'lateral': 2, 'meia': 3, 'atacante': 2, 'tecnico': 1},
        '5-4-1': {'goleiro': 1, 'zagueiro': 5, 'lateral': 2, 'meia': 4, 'atacante': 1, 'tecnico': 1},}
    
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
    
    escalacao = escalacoes[escalacao - 1]
    quantidades_atletas = quantidades_escalacao[escalacao]
                
    return escalacao, quantidades_atletas

def definir_selecao(dicCartola, quantidades_atletas):
    
    selecao_atletas = {} # Criar variavel para armazenar a seleção.
    atletas = dicCartola.get('atletas', []) # .get para evitar erro caso a chave não exista ou esteja corrompida.
    if not atletas:
        sys.exit('ERR0: Não existem atletas disponíveis no dicionário do Cartola FC.')
    clubes = dicCartola.get('clubes', {})
    posicoes = dicCartola.get('posicoes', {})
    if not clubes or not posicoes:
        sys.exit('ERR0: Dados de clubes ou posições estão incompletos no dicionário do Cartola FC.')
    
    # Filtrar e ordenar os atletas por pontuação em cada posição.
    atletas_por_posicoes = {}
    for atleta in atletas:
        posicao_id = atleta.get('posicao_id')
        if posicao_id not in atletas_por_posicoes:
            atletas_por_posicoes[posicao_id] = []
    
    # Calculo da pontuação: média * jogos ( 'media_num' * 'jogos_num' ).
        pontuacao_media = atleta.get('media_num', 0) * atleta.get('jogos_num', 0)
        atleta['pontuacao'] = pontuacao_media
        atletas_por_posicoes[posicao_id].append(atleta)

    # Organizando nomes de posições para id.
    nome_posicao_id = {}
    for posicao_id, posicao_info in posicoes.items():
        nome_posicao_id[posicao_info['nome'].lower()] = int(posicao_id)

    # Ordenar por posição.
    ordem = ['goleiro', 'zagueiro', 'lateral', 'meia', 'atacante', 'tecnico']
    for nome_posicao in ordem:
        posicao_id = nome_posicao_id.get(nome_posicao)
        if not posicao_id:
            continue
        qtd = quantidades_atletas.get(nome_posicao, 0)
        if qtd == 0:
            continue

    # selecionar os melhores atletas das posições.
        lstselecao = sorted(atletas_por_posicoes.get(posicao_id, []),key=lambda x: x['pontuacao'], reverse=True)
        for atleta in lstselecao[:qtd]:
            atleta_id = atleta.get('atleta_id')
            nome_atleta = atleta.get('nome', ' ')
            apelido_atleta = atleta.get('apelido', ' ')
            foto_aleta = atleta.get('foto', ' ')
            # correção da URL da foto.
            if '_FORMATO_' in foto_aleta:
                foto_aleta = foto_aleta.replace('_FORMATO_', '_220x220_').replace('_FORMATO', '_220x220')
            clube_id = atleta.get('clube_id')
            clube_nome = clubes.get(clube_id, {}).get('nome_fantasia', ' ')
            escudo = clubes.get(clube_id, {}).get('escudos', {}).get('60x60','')
            pos_nome = posicoes.get(str(posicao_id), {}).get('nome', '')
            pontuacao = atleta['pontuacao']
            selecao_atletas[atleta_id] = {
                'id': atleta_id,
                'nome': nome_atleta,
                'apelido': apelido_atleta,
                'foto': foto_aleta,
                'clube': clube_nome,
                'escudo': escudo,
                'posicao_id': posicao_id,
                'posicao_nome': pos_nome,
                'pontuacao': pontuacao}
            
    return selecao_atletas, ordem

def salvar_exibir_selecao(selecao_atletas, ano, ordem):
    #salvar seleção em arquivo JSON.
    strselecao_json = f'cartola_selecao_{ano}.json'
    try:
        with open(strselecao_json, 'w', encoding='utf-8') as arquivo_json:
            json.dump(selecao_atletas, arquivo_json, ensure_ascii=False, indent=4)
        print(f'Arquivos "{strselecao_json}" salvos com sucesso!')
    except Exception as e:
        sys.exit(f'ERR0: {e}')
        return
    
    # exibir seleção.
    print("\n---Seleção do Cartola FC ---")
    for posicao in ordem:
        for atleta in selecao_atletas.values():
            if atleta['posicao_nome'].lower() == posicao.lower():
                print(f"{atleta['posicao_nome']}: {atleta['nome']} ({atleta['apelido']}) - {atleta['clube']} - Pontuação: {atleta['pontuacao']:.2f}")