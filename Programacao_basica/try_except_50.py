idade = ...

while idade == ...:
    try:
        idade = int(input('Digite sua idade: '))
        print('Número inserido É UM número inteiro')
    except ValueError:
        print('Número inserido NÃO É UM número inteiro')

print('Concluído')