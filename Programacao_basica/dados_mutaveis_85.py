nome = 'luiz'
nome = 'joão'

print(nome)

lista_a = ['Luiz', 'Maria']
lista_b = lista_a

lista_a[0] = 'Lucas'
print(lista_a)
print(lista_b)

lista_b[0] = 'Fernando'

print(lista_a)
print(lista_b)


lista_a = ['Luiz', 'Maria']
lista_b = lista_a.copy()

lista_b[0] = 'Gustavo'

print(lista_a)
print(lista_b)