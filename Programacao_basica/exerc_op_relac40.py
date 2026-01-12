primeiro_valor = input('Digite primeiro valor: ')
segundo_valor = input('Digite segundo valor: ')

if primeiro_valor > segundo_valor:
    print(f'primeiro valor: {primeiro_valor} é maior ao segundo valor: {segundo_valor}')
elif primeiro_valor == segundo_valor:
    print(f'primeiro valor: {primeiro_valor} é igual ao segundo valor: {segundo_valor}')
else:
    print(f'primeiro valor: {primeiro_valor} é menor ao segundo valor: {segundo_valor}')