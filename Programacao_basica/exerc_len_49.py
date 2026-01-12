nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if (not nome.isdigit() and idade.isdigit()) and (nome.strip() != '' and idade.strip() != ''):
    print(f'Seu nome é  {nome}')
    print(f'Seu nome invertido é:  {nome[::-1]}')
    
    if '' in nome :
        print(f'Seu nome contém espaços {nome}')
    else: 
        print(f'Seu nome não contém espaços {nome}')

    print(f'Seu nome tem {len(nome)} caractéres')
else:
    print('Nome não pode ser um número e idade não pode ser letra')
