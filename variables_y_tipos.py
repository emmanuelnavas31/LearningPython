def variables():
    '''
        • Usamos un simbolo = para asignar un valor a una variable
        • El tipo de nombre de la variable se realiza con asignaciones en minusculas, nunca inician con mayuscula
        se puede usar camelCase o guion_al_piso
        • Los tipos de datos los podemos inicializar con comillas sencillas o comillas dobles
    '''

    name = 'Harold Emmanuel'  # Valores string o cadena de caracteres
    print(f'Variable nombre {name} tipo de dato = {type(name)}')

    age = 27  # Valores enteros
    print(f'Variable edad {age} tipo de dato = {type(age)}')

    price = 15.28  # Tipo de dato flotante, lo que significa que puede tener decimales
    print(f'Variable price {price} tipo de dato = {type(price)}')

    status = False  # Tipo de valor booleano (True, False) verdadero o falso
    print(f'Variable status {status} tipo de dato = {type(status)}')

    '''
        Funciones de input para poder solicitar datos.
    '''
    my_name = str(input('Ingrese su nombre: '))
    my_age = int(input('Ingrese su edad: '))
    print(f'El nombre ingresado es: {my_name} y el tipo de dato es {type(my_name)}, edad: {my_age} y el tipo de dato es {type(my_age)}')


if __name__ == '__main__':
    variables()
