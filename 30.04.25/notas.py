# Calcular média da disciplina do IFRN
#
# 1) Soliticar ao usuário que informe duas notas (As notas são inteiras)
# 2) Calcular a média do IFRN
# 3) Exibir a média sem casa decimal

nota1 = int(input(' Digite a nota1'))
nota2 = int(input(' Dgiite a nota2'))

média = ( nota1 * 2 + nota2 * 3 ) / 5

print( f'Essa é sua nota {média:.0f}')