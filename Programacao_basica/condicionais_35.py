#if / elif / else
# se / se não se / se não

while True:
    entrada = input('Você quer "Entrar" ou "Sair"?: ').casefold()

    if entrada in ('entrar'):
        print(f'Você entrou no sistema')
        break
    elif entrada in ('sair'):
        print('Você saiu do sistema')
        break
    else:
        print('Você não escolheu nenhuma das opções')

print('Fora do bloco do WHILE')

# while True :
    
#     entrada = input('Você quer "Entrar" ou "Sair"?: ').casefold()

#     if entrada == 'entrar':
#         print('Você entrou no sistema')
#         break

#     elif entrada == 'sair':
#         print('Você saiu do sistema')
#         break

#     else:
#         print('Você não escolheu nenhuma das opções')
#         entrada = ''
