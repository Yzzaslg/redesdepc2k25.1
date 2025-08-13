'''Pesquise na Internet uma API pública (gratuita ou com plano gratuito) que possa ser utilizada em aplicações de software. 
Em seguida, desenvolva um programa em Python que utilize essa API para demonstrar alguma funcionalidade.'''

# Pesquisa e documentação:
# Informe o nome da API escolhida: Lyrics.ovh
# Explique o que a API fornece (quais dados ou serviços): A API retorna a letra de músicas a partir do nome do artista e do título da música.
# Indique a documentação consultada (link oficial ou repositório): https://lyricsovh.docs.apiary.io

# Descreva o objetivo do seu programa: o que ele fará utilizando essa API.:
# O usuário poderá pesquisar letras de músicas informando artista e título, as letras serão exibidas e salvas em um histórico, permitindo depois visualizar ou carregar esse histórico.

import sys
from Q4_funcoes import menu_opcoes, buscar_letra, exibir_letra, atualizar_salvar_historico, carregar_historico

historico = []  # Lista para armazenar o histórico de buscas

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
            print('ERR0: Por favor, digite um número válido.')
        except Exception as e:
            print(f'ERR0: {e}')
        
    if opcao == 1:
        print('Buscando letra da música...')
        while True:
            artista = input('Digite o nome do artista: ').strip()
            musica = input('Digite o título da música: ').strip()
            if not artista or not musica:
                print('ERR0: Artista e título da música não podem ser vazios.')
                continue # volta para o inicio do loop onde solicita artista ou música novamente.
                
            letra = buscar_letra(artista, musica)
            if not letra:
                print(f'ERR0: Letra não encontrada para a música "{musica}" do artista "{artista}".')
                continue # volta para o inicio do loop também.
            else:
                exibir_letra(artista, musica, letra)

            # Adiciona a solicitação ao histórico.
                historico.append({'artista': artista, 'musica': musica, 'letra': letra})
                break
        
    elif opcao == 2:
        print('Exibindo histórico...')
        if historico:
            for i, item in enumerate(historico, start=1):
                print(f'{i}. {item['artista']} - {item['musica']}')
        else:
            print('\nHistórico vazio. Nenhuma pesquisa realizada.')

    elif opcao == 3:
        print('Salvando histórico atual...')
        atualizar_salvar_historico(historico)

    elif opcao == 4:
        historico_json = 'historico_lyrcis.json'
        print('Carregando histórico...')
        historico = carregar_historico(historico_json)
        if historico:
            print(f'Histórico carregado com sucesso, ({len(historico)} registros).')
        else:
            print('\nHistórico vazio ou não encontrado.')

    elif opcao == 5:
        print('Saindo do programa...')
        break
    else:
        print('Opção inválida, escolha novamente.')



