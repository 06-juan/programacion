n = int(input('introduce un numero positivo para calcular su factorial: '))
factorial=1

if n != 0:
    for i in range(n):
        factorial *= i+1
    print(f'el factorial de {n} es {factorial}')
else:
    print(f'el factorial de 0 es 1')
