N = int(input(' Introduce n positivo para calcular los n primeros terminos de fibonacci: '))
termino=1
termino1=0
termino2=0

if termino > 0:
    print(termino)
else:
    print(0)

for i in range(N):
    termino += termino1
    print(termino)
    termino1 = termino-termino2
    termino2=termino1