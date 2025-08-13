'''Pesquise na Internet uma API pública (gratuita ou com plano gratuito) que possa ser utilizada em aplicações de software. 
Em seguida, desenvolva um programa em Python que utilize essa API para demonstrar alguma funcionalidade.'''

# Pesquisa e documentação:
# Informe o nome da API escolhida: Steam Web API + Steam Storefront API
# Explique o que a API fornece (quais dados ou serviços): A API retorna informações sobre jogos, incluindo nome, descrição, preço, lançamento e outros detalhes.
# Indique a documentação consultada (link oficial ou repositório): https://api.steampowered.com/ISteamApps/GetAppList/v2/ ( busca jogos pelo nome e retorna uma lista de com jogos e seus appid ) e https://store.steampowered.com/api/appdetails ( busca informações de um jogo na Steam usando o AppID ).
# Descreva o objetivo do seu programa: o que ele fará utilizando essa API.:
# O usuário poderá pesquisar jogos pelo nome, ver uma lista de resultados, selecionar o jogo e visualizar informações detalhadas.
import sys
from Q4_funcoestwo import menu_opcoes, buscar_jogo, consultar_app_id_jogo, exibir_detalhes_jogo, atualizar_salvar_historico, carregar_historico

arquivo_historico = 'historicosteam.json'
historico = []  # Lista para armazenar o histórico de pequisas.

while True:
    menu_opcoes()
    while True:
        try:
            opcao = int(input('\nEscolha uma das opções do menu (1-5): '))
            if 1 <= opcao <= 5:
                break
            else:
                print(f'ERR0: Opção inválida. Escolha uma das opções do menu (1-5): ')
        except ValueError:
            sys.exit('ERR0: Por favor, digite um número válido.')
        except Exception as e:
            sys.exit(f'ERR0: {e}')
    
    # Buscar informações de jogo.
    if opcao == 1:
        print('Buscando informações de jogo...')
        while True:
            nome_jogo = input('Digite o nome do jogo ou 0 para voltar: ').strip()
            if nome_jogo == '0':
                break  # Se o usuário digitar 0, volta para o início do loop.
            # Verifica se o nome do jogo não está vazio.
            if not nome_jogo:
                print('ERR0: O nome do jogo não pode ser vazio.')
                continue  # Volta para o início do loop onde solicita o nome do jogo novamente.
                
            jogos_encontrados = buscar_jogo(nome_jogo)
            if not jogos_encontrados:
                print(f'ERR0: Nenhum jogo encontrado com o nome "{nome_jogo}".')
                continue  # Volta para o início do loop também.
            else:
                print('\nJogos encontrados:')
                for i, (app_id, name) in enumerate(jogos_encontrados, start=1):
                    print(f'{i}. {name} (AppID: {app_id})')
                
                while True:
                    try:
                        escolha = int(input('\nEscolha o número do jogo para ver detalhes ou 0 para voltar: '))
                        if escolha == 0:
                            break
                        elif 1 <= escolha <= len(jogos_encontrados):
                            app_id = jogos_encontrados[escolha - 1][0]
                            info_jogo = consultar_app_id_jogo(app_id)
                            if info_jogo:
                                exibir_detalhes_jogo(info_jogo)
                                historico.append({'nome': info_jogo['name'], 'app_id': app_id})
                            break
                        else:
                            print('ERR0: Opção inválida. Escolha um número válido.')
                    except ValueError:
                        sys.exit('ERR0: Por favor, digite um número válido.')
                    except Exception as e:
                        sys.exit(f'ERR0: {e}')
                        break

    # Ver histórico atual.
    elif opcao == 2:
        print('Exibindo histórico...')
        if historico:
            for i, item in enumerate(historico, start=1):
                print(f'{i}. {item["nome"]} (AppID: {item["app_id"]})')
        else:
            print('\nHistórico vazio. Nenhuma pesquisa realizada.')
    
    # Salvar histórico no arquivo.
    elif opcao == 3:
        print('Salvando histórico atual...')
        atualizar_salvar_historico(historico, arquivo_historico)
    
    # Carregar histórico de arquivo.
    elif opcao == 4:
        print('Carregando histórico...')
        historico_json = 'historicosteam.json'
        historico = carregar_historico(historico_json)
        if historico:
            print(f'Histórico carregado com sucesso, ({len(historico)} registros).')
        else:
            print('\nHistórico vazio ou não encontrado.')
    
    # Sair do programa.
    elif opcao == 5:
        print('Saindo do programa...')
        break
    else:
        print('ERR0: Opção inválida, escolha novamente.')