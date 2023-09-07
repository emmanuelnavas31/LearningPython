"""
    Proceso de loops
    1. While
    2. Ciclos FOR

"""


def loops():
    counter = 0
    # Mientras el contador sea menor a 10 se va a ejecutar
    while counter < 30:
        counter += 1

        if counter == 15:
            # break # Detengo la ejecucion del while
            continue  # Salta la iteracion en la que va y continua con el ciclo
        print('Ejecucion', counter)

    counter2 = 0
    while counter2 < 30:
        counter2 += 1
        if counter2 < 15:
            continue
        print("Continue 2 ", counter2)


def fors():
    for element in range(1, 21):
        print("for element ", element)

    list_example = [1, 5, 78, 14, 85, 63, 25]
    for num in list_example:
        print(f"Elemento numero = {num}")

    tuple_example = ('harold', 'emmanuel', 'navas')
    for tuples in tuple_example:
        print(f'Tuples value = {tuples}')

    product = {
        'name': 'Camisa',
        'price': 100,
        'stock': 89
    }
    for i in product:
        print(f"Elemento = {i} => {product[i]}")
    for key, value in product.items():
        print(f"Clave valor = {key} => {value}")
    people = [
        {
            'name': 'Emmanuel',
            'age': 27
        },
        {
            'name': 'harold',
            'age': 28
        },
        {
            'name': 'Roberto',
            'age': 56,
        }
    ]
    for person in people:
        print(f'Personas: {person}')
        print('name => ', person['name'])
        print('Edad => ', person['age'])

    my_list = [1, -1, 2, -2, 3, -3, 4, -4]
    new_list = []
    for mlist in my_list:
        if mlist >= 1:
            new_list.append(mlist)

    print(new_list)

    # Ciclos anidados
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("matriz", matriz[0]) # Apuntamos a ma matriz 1
    print("matriz", matriz[0][1]) # Apuntamos a ma matriz 1 y a la posicion 1
    for element in matriz:
        print("Los elementos son = ", element)
        for item in element:
            print(f"Elementos = {item}")

if __name__ == '__main__':
    loops()
    fors()
