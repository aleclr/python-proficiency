n = int(input('Informe o número de botas entregues: '))

botas = ''
count = 0
while count < n :
    if count == (n - 1):    
        bota = input('Informe uma das botas: ')
        botas += bota
    else:
        bota = input('Informe uma das botas: ')
        botas += bota + ','
    count += 1

print(type(botas), botas)
array_botas = botas.split(',')
print(array_botas)

pares = 0
count = 0
while count < n :
    proxima = 1
    bota_atual = array_botas[count]
    possivel_par = array_botas[proxima]
    while (bota_atual[0] + bota_atual[1] != possivel_par[0] + possivel_par[1]) and (proxima < n):
        print('botas comparação: ' + bota_atual, possivel_par)
        proxima += 1
        possivel_par = array_botas[proxima]
    if bota_atual[0] + bota_atual[1] == possivel_par[0] + possivel_par[1]:
        print('botas pós comparação: ' + bota_atual, possivel_par)
        if bota_atual[3] != possivel_par[3]:
            pares += 1
    count += 1

print(f'O total de pares que podem ser formados é {pares}')