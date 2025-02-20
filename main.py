'''
print('Hola mundo')
nombre= input('¿Como te llamas? ')
edad = eval(input('¿cual es tu edad? '))
print(f'Hola! {nombre} sabias que tu edad es {2025-edad}')
'''

for i,j in enumerate\
(['juan','sofi','sam']):
    print(i+1,j)


for i,j,k in zip(['juan','sofi','sam'],[100,200,300],['colombia','peru','ecuador']):
    print(i,j,k)