import os, sys, requests, json

diretorio = os.path.dirname(__file__)

arquivo_historico = 'historicosteam.json'

def menu_opcoes():
    print('\nBem-vindo ao programa steamgames!')
    print('\n===== MENU PRINCIPAL =====')
    print('\nEscolha uma opção do menu:')
    print('\n1 - Buscar informações de jogo')
    print('2 - Ver histórico atual')
    print('3 - Salvar histórico no arquivo')
    print('4 - Carregar histórico de arquivo')
    print('5 - Sair\n')
    print('=' * 30)

def buscar_jogo(nome_jogo): # Busca jogos na API da Steam pelo nome e retorna uma lista de com jogos e seus appid.
    URLsteam = f'https://api.steampowered.com/ISteamApps/GetAppList/v2/'
    try:
        resposta = requests.get(URLsteam, timeout=10)
        resposta.raise_for_status()  # Gera erro se status_code != 200
        dicjogos_nome = resposta.json()['applist']['apps']
        jogos_encontrados = [(jogo['appid'], jogo['name'])
            for jogo in dicjogos_nome
            if nome_jogo.lower() in jogo['name'].lower()]
        return jogos_encontrados
    except requests.Timeout:
        print('ERR0: A requisição demorou mais do que esperado e foi cancelada (timeout).')
        return []
    except requests.RequestException as e:
        print(f'ERR0: Falha na requisição à API: {e}')
        return []

def consultar_app_id_jogo(app_id): # Busca informações de um jogo na Steam usando o AppID.
    URLsteam = f'https://store.steampowered.com/api/appdetails?appids={app_id}&l=portuguese'
    try:
        resposta = requests.get(URLsteam, timeout=10)
        resposta.raise_for_status()  # Gera erro se status_code != 200
        dicinfo_jogo = resposta.json()
        if dicinfo_jogo.get(str(app_id), {}).get('success'): # 1º .get: pega a chave do jogo no JSON (cada jogo vem identificado pelo seu appid) e o 2º .get: verifica se a API indicou que a consulta foi bem-sucedida.
            return dicinfo_jogo[str(app_id)]['data']
        else:
            print(f'Nenhuma informação pública disponível para o jogo com AppID {app_id}, \npode haver restrição regional, de idade ou se o jogo foi removido/vendido de outra forma.')
            return None
    except requests.Timeout:
        print('ERR0: A requisição demorou demais e foi cancelada (ERR0: timeout).')
        return None
    except requests.RequestException as e:
        print(f'ERR0: Falha na requisição à API: {e}')
        return None
    
def exibir_detalhes_jogo(info_jogo): # Exibe informações relevantes de um jogo.
    print('\n' + '='*50)
    print(f"Nome: {info_jogo['name']}")
    print(f"Descrição: {info_jogo.get('short_description', 'Sem descrição disponível.')}")
    print(f"Preço: {info_jogo.get('price_overview', {}).get('final_formatted', 'Gratuito')}")
    print(f"Data de lançamento: {info_jogo.get('release_date', {}).get('date', 'Data não disponível')}")
    print('\n' + '='*50)

def atualizar_salvar_historico(historico, arquivo_historico):
    historicosteam = f'{diretorio}\\{arquivo_historico}'
    # Atualiza o histórico e salva em um arquivo JSON.
    try:
        with open(historicosteam, 'w', encoding='utf-8') as arquivo_historico:
            json.dump(historico, arquivo_historico, ensure_ascii=False, indent=4)
        print(f'Histórico atualizado e salvo no arquivo: "{arquivo_historico}" com sucesso!')
    except Exception as e:
        sys.exit(f'ERR0: {e}')

def carregar_historico(arquivo_historico):
    # Carrega o histórico de um arquivo JSON.
    try:
        with open(arquivo_historico, 'r', encoding='utf-8') as arquivo_historico:
            historico = json.load(arquivo_historico)
        return historico
    except FileNotFoundError:
        print(f'ERR0: Arquivo "{arquivo_historico}" não encontrado.')
        return []
    except json.JSONDecodeError:
        print(f'ERR0: Erro ao decodificar o JSON do arquivo "{arquivo_historico}".')
        return []