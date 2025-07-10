import os

strDir = os.path.dirname(__file__)

try:
   arqLeitura = open(f'{strDir}\\carta.txt', 'r', encoding='utf-8')
except FileNotFoundError:
   print('\nERRO: Arquivo não encontrado...')
except Exception as erro:
   print(f'\nERRO: {erro}')
else:
   while True:
      strConteudo = arqLeitura.readline()
      if not strConteudo: break
      print('-'*80)
      print(strConteudo.strip())
   arqLeitura.close()