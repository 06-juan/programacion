n = int(input('Introduce el numero n positivo: '))
suma = 0

if n != 0:
    for i in range(n):
        suma += i+1
    print(f' la {n}-esima suma es {suma}')

else:
    print(f'la 0-esima suma es {suma}')