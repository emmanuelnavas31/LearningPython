"""
    Los tipos de datos se pueden transformar de forma dinamica de acuerdo a las necesidades que se tengan pero
    se tiene que tener cuidado y no se recomienda usar tanto estas transformaciones por que los resultados
    pueden llegar a ser alterados
"""


def transformaciones():
    name = 'Emmanuel'
    print(f'Nombre = {name} de tipo {type(name)}')

    name = 12
    print(f'Nombre = {name} de tipo {type(name)}')

    name = False
    print(f'Nombre = {name} de tipo {type(name)}')

    # Concatenacion de strings
    print('Harold ' + 'Navas')

    print(20 + 10)

    # No se puede concatenar un String Con un numero
    # print('20' + 10)
    age = 12
    print("Mi edad es " + str(age))
    print(f"Mi edad es {age}")

    newage = int(input('Ingrese su edad por favor: ')) # Este valor viene como un string pero podemos obligar a que el dato se ingrese como un entero
    # La otra forma en la que podemos transformar el string en un entero siempre y cuendo sea un numero sin decimales
    # es reasignando la misma variable pero con un tipo de dato distinto el cual quedaria de la siguiente manera newage = int(newage)
    print(f'Tu edad es {newage} y sera de {newage + 10} en 10 years y el tipo de dato es {type(newage)}')


if __name__ == '__main__':
    transformaciones()
