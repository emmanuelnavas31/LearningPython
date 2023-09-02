def condicionales():
    mascota = input('Cual es tu mascota favorita: ')
    if mascota == 'perro':
        print('Genial')
    elif mascota == 'gato':
        print('Super')
    else:
        print('Que aburrido!')

    stock = int(input('Ingrese un stock: '))
    if stock >= 100 and stock <= 1000:
        print('El stock es correcto')

    else:
        print('El stock no es correcto')

    # Ejercicio, Crear un sistema de validacion de que si un numero es par o impar

    parimpar = int(input('Ingrese un numero para saber si el numero es par o impar: '))
    if parimpar % 2 == 0:
        print('El numero es par')
    elif parimpar % 2 != 0:
        print('El numero no es par')

if __name__ == "__main__":
    condicionales()
