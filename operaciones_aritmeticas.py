def operacionesaritmeticas():
    '''
    Orden logico de como se solucionan las operaciones aritmeticas

    P - Parentesis
    E - Exponentes
    M - Multiplicacion
    D - Division
    A - Adicion
    S - Sustraccion
    '''
    numero1 = 10
    numero2 = 2

    # Suma
    print(f'Suma: {numero1 + numero2}')

    # Resta
    print(f'Resta: {numero1 - numero2}')

    # Multiplicacion
    print(f'Multiplicacion: {numero1 * numero2}')

    # Division
    print(f'Division: {numero1 / numero2}')

    # Modulo o residuo
    print(f'Modulo o residuo: {numero1 % numero2}')

    # Division con valor entero
    print(f'Division con valor entero: {numero1 // numero2}')

    # Exponente
    print(f'Exponente: {numero1 ** numero2}')

    # Entre los operadores que pueden multiplicarse con los strings es la multiplicacion
    print('Hola mundo, ' * 3)

    # Operacion
    print('Resultado ', 2 ** 3 + 3 - 7 / 1 // 4)
    # La solucion de la informacion generada es
    print('1 Exponentes: ', 2 ** 3)
    print('2 Division: ', (7 / 1) // 4)
    print('3 suma: ', 8 + 3)
    print('4 Resta: ', 11 - 1)
    # Las divisiones en cero no son permidas
    

if __name__ == "__main__":
    operacionesaritmeticas()
