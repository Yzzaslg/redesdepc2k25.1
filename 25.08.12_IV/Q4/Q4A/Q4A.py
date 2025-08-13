'''Pesquise na Internet uma API pública (gratuita ou com plano gratuito) que possa ser utilizada em aplicações de software. 
Em seguida, desenvolva um programa em Python que utilize essa API para demonstrar alguma funcionalidade.'''

# Pesquisa e documentação:
# Informe o nome da API escolhida: Steam Web API + Steam Storefront API
# Explique o que a API fornece (quais dados ou serviços): A API retorna informações sobre jogos, incluindo nome, descrição, preço, lançamento e outros detalhes.
# Indique a documentação consultada (link oficial ou repositório): https://api.steampowered.com/ISteamApps/GetAppList/v2/ ( busca jogos pelo nome e retorna uma lista de com jogos e seus appid ) e https://store.steampowered.com/api/appdetails ( busca informações de um jogo na Steam usando o AppID ).
# Descreva o objetivo do seu programa: o que ele fará utilizando essa API.:
# O usuário poderá pesquisar jogos pelo nome, ver uma lista de resultados, selecionar o jogo e visualizar informações detalhadas.
import sys
from Q4_funcoestwo import menu_opcoes

menu_opcoes()