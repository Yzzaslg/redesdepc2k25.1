import os, sys, requests, json

def menu_opcoes():
    print('\nBem-vindo ao programa lyrics!')
    print('\n===== MENU PRINCIPAL =====')
    print('\nEscolha uma opção do menu:')
    print('\n1 - Buscar letra de música')
    print('2 - Ver histórico atual')
    print('3 - Salvar histórico no arquivo')
    print('4 - Carregar histórico de arquivo')
    print('5 - Sair\n')
    print('=' * 30)

def buscar_letra(artista, musica):
# Busca a letra de uma música usando a API lyrics.ovh.
    strURLlyrics = f'https://api.lyrics.ovh/v1/{artista}/{musica}'
    try:    
        dicAPIlyrics = requests.get(strURLlyrics, timeout=5).json()
        if 'lyrics' in dicAPIlyrics:
            return dicAPIlyrics['lyrics']
        else:
            return 'Letra não encontrada.'
    except requests.Timeout:
        print('ERR0: A requisição demorou demais e foi cancelada (timeout).')       
    except requests.RequestException as e:
        sys.exit(f'ERR0: Falha na requisição à API: {e}')

def exibir_letra(artista, musica, letra): # Exibir a letra de forma bonita ( formatada ).
    print('\n' + '='*50)
    print(f'Música: {musica} | Artista: {artista}')
    print('='*50)
    print(letra)
    print('='*50)

diretorio = os.path.dirname(__file__)

def atualizar_salvar_historico(historico):
    strhistoricolyrcis = f'{diretorio}\\historico_lyrcis.json'
    # Atualiza o histórico e salva em um arquivo JSON.    
    try:
        with open(strhistoricolyrcis, 'w', encoding='utf-8') as arquivo_json:
            json.dump(historico, arquivo_json, ensure_ascii=False, indent=4)
        print(f'Histórico atualizado e salvo no arquivo: "{strhistoricolyrcis}" com sucesso!')
    except Exception as e:
        sys.exit(f'ERR0: {e}')

def carregar_historico(strhistoricolyrcis):
    # Carrega o histórico de um arquivo JSON.
    try:
        with open(strhistoricolyrcis, 'r', encoding='utf-8') as arquivo_json:
            historico = json.load(arquivo_json)
        return historico
    except FileNotFoundError:
        print(f'ERR0: Arquivo "{strhistoricolyrcis}" não encontrado.')
        return []
    except json.JSONDecodeError:
        print('ERR0: Erro ao decodificar o JSON do arquivo.')
        return []


    
