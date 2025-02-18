semestre= int(input('¿Que semestre esta cursando? '))
R=''


if semestre > 5 and semestre < 9:

    while True:
        R = input ('¿Ya estas en un grupo de investigación? S/n ')

        if R == 's' or R =='S' or R == 'n' or R == 'N':
            break

    if R == 's' or R == 'S':
        print('Felicidades lo estas haciendo bien')

    elif R == 'n' or R == 'N':
        print('animate a hacerlo')

    else:
        print ('Respuesta no valida')
    
if semestre > 1 and semestre < 6:

    while True:
        R = input('¿Has perdido materias? S/n ')

        if R == 's' or R =='S' or R == 'n' or R == 'N':
            break
    
    if R == 's'or R == 'S':
        
        while True:
            R2 = input('¿Alguna de esas tiene prerequisitos? S/n ')

            if R2 == 's' or R2 =='S' or R2 == 'n' or R2 == 'N':
                break

        if R2 == 's'or R2 == 'S':
            print('¡Recuerda quedebes nivelarte para pasar a sexto semestre!')

        else:
            print('¡Recuerda quedebes estar nivelado para pasar a sexto semestre!')

    else:
        print('Excelente vas muy bien')

if semestre == 9 or semestre == 10:
    print ('Ponte pilas con la tesis')

if semestre > 10:
    print(f'Tu tesis no podra obtener distinción por tus {semestre-10} semestres extras')

if semestre == 1:
    print('eres un baby')