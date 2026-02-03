pessoa = {
    'nome': 'Luiz',
    'sobrenome': 'miranda',
    'idade': 18,
    'altura': 1.8,
    'endereco': [
        {'rua': 'rua 1', 'numero': '01'},
        {'rua': 'rua 2', 'numero': '02'}
    ],
}

print(pessoa, type(pessoa))
print(pessoa['altura'])
print(pessoa['nome'])
print(pessoa['endereco'])


print('')

for chaves in pessoa:
    print(chaves)

print('')

for chaves in pessoa:
    print(chaves, pessoa[chaves])