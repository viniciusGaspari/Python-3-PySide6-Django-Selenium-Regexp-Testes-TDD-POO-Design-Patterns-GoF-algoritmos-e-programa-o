"""
Interpolação básica de strings

s - string
d e i - int
f - float
x e x - Hexadecimal (ABCDE123456789)

"""

nome = 'Luiz'
preco = 1000.09885
variavel = '%s, o preço total foi R$%.2f' % (nome, preco)
print(variavel)

print('O hexadecimal de %d é %04x' % (15, 15))