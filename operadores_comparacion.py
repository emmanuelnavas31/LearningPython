"""
    Los operadores de comparacion son importantes para los flujos de trabajo
"""


def comparacion():
    numero1 = 45
    numero2 = 60

    # Mayor
    print(f'Signo mayor: {numero1} > {numero2}', numero1 > numero2)

    # Menor
    print(f'Signo menor: {numero1} < {numero2}', numero1 < numero2)

    # Mayor o Igual
    print(f'Signo mayor o igual: {numero1} >= {numero2}', numero1 >= numero2)

    # Menor o Igual
    print(f'Signo menor o igual: {numero1} <= {numero2}', numero1 <= numero2)

    # Igual
    print(f'Signo igual: {numero1} == {numero2}', numero1 == numero2)

    # Diferente
    print(f'Diferente: {numero1} != {numero2}', numero1 != numero2)

    '''
        Aparte de realizar comparativas de numeros tambien podemos realizar comparativas 
        entre valores string (Cadenas de textos)
    '''
    # Comparando textos y numeros
    print(f"Comparando texto: {'Harold' == 'harold'}")
    print(f"Comparando texto: {'Harold' == 'Harold'}")
    print(f"Comparando numeros: {10 == '10'}")
    print(f"Comparando numeros: {10 == 10}")

    '''
        Comparacion de valores flotantes
    '''
    flotante1 = 3.3
    print(f'Valor flotante flotante1: {flotante1}')
    flotante2 = 1.1 + 2.2
    print(f'Valor flotante flotante2: {flotante2}')

    # La igualacion de valores en este caso nos dara False ya que el numero de digitos generados en decimales por la sumatoria
    print(f'Igualacion de flotante {flotante1 == flotante2}')

    # Establecemos el formato para la cantidad de digitos que queremos que aparezcan para las comparaciones
    flotante3 = format(flotante2,
                       '.2g')  # Establecemos 2 digitos decimales convertido en string primero y luego asignando
    print(
        f'Igualacion de flotante con modificacion de decimales {flotante3} y flotante1 == flotante3? {str(flotante1) == flotante3}')

    # Realizamos la transformacion de datos a flotantes y no string, realizamos la transformacion matematica
    tolerancia = 0.00001
    print(f'Informacion del valor = {abs(flotante1 - flotante2) < tolerancia}')


if __name__ == '__main__':
    comparacion()
