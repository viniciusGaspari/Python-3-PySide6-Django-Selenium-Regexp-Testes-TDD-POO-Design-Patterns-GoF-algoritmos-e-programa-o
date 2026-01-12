from Pessoa import Pessoa

nome1 = 'Vinicius'
nome2 = 'Maria'

idade1 = 22
idade2 = 33


p1 = Pessoa(nome1, idade1)
p2 = Pessoa(nome2, idade2)

print(p1.getNome(), p1.getIdade())
print(p2.getNome(), p2.getIdade())

lista_p = [p1, p2]

for pessoas in lista_p:
    print(f'Nome: {pessoas.getNome()} | idade: {pessoas.getIdade}')