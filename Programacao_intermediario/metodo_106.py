def Print():
    print('Varias')


Print()

def ola(nome: str='Sem nome'):
    print(f'Olá, {nome}')
    
    if not isinstance(nome, str):
        raise TypeError('Nome é por letras')

ola('Rogerio')
ola()
