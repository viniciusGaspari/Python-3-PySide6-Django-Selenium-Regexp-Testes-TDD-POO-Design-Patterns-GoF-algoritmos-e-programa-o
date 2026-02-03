n1 = int(input('Digite primeiro número: '))
n2 = int(input('Digite segundo número: '))
operacao = input('Digite tipo de operação: (s)oma, (m)ultiplicacao, (su)ubtracao ')

def soma(n1, n2):
    return n1 + n2

def multipliacao(n1, n2):
    return n1 * n2

def subtracao(n1, n2):
    return n1 - n2

def calculo(operacao):
    if operacao == 's' or operacao == 'su' or operacao == 'm':
        if operacao in ('s'):
            return soma(n1, n2) 
        if operacao in ('m'):
            return multipliacao(n1, n2)
        if operacao in ('su'):
            return subtracao(n1, n2)
    else:
        return 'Solicitação de operação inválida'

print(calculo(operacao))

# def criar_saudacao(saudacao, nome):
#     def saudar():
#         return f'{saudacao}, {nome}'
#     return saudar

# print(criar_saudacao('bom dia', 'luiz')())
# print(criar_saudacao('boa noite', 'maria'))