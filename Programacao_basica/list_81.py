String = 'ABCDE'

lista = ['a', 2]

print(lista)
print(lista[0])
print(lista[1])

carrinho = [{id': '1', 'produto': 'panela', 'isOferta': F'alse}, 
            [{'id': '2', 'produto': 'lápis', 'isOferta': True}]]
print(carrinho[0])
print(carrinho[1])
carrinho = [{"id": 1, "produto": "panela"}]

# Alterando o valor da chave 'produto' do primeiro item
carrinho[0][1] = "frigideira"

print(carrinho)
