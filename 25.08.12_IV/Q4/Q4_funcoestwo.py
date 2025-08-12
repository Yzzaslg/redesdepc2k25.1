import os, sys, requests, json

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