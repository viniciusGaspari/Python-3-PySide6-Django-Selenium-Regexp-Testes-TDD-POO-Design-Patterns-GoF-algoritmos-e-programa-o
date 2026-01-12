contador = 0

while contador < 30:
    contador += 1

    if contador == 5: 
        print('Não vou mostrar o', contador)
        continue

    if contador >= 10 and contador <= 27:
        print('Não vou mostrar o', contador)
        continue
    
    print(contador)

print('Acabou')

