nome = 'Vinicius'
peso = 110
altura = 178945.6
imc = peso / altura ** 2

linha_1 = f'{nome} tem {altura:,.10f} de altura'
print(linha_1)

print()

altura = 1.78
imc = peso / altura ** 2
print(f'{nome} tem {altura} de altura')
print(f'pesa {peso} quilos e seu IMC é:  {int(imc)}')