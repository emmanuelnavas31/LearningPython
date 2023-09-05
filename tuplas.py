def tuplas():
    """
        Las tuplas son elementos no mutables significa que su edicion
        es limitada a comparacion de las listas.
    :return:
    """
    numbers = (1, 2, 3, 4, 5, 6)
    string = ('hola', 'mundo', 'hola', 'mundo', 'harold')

    print(f"Numeros = {numbers}, tipo {type(numbers)}")
    print(f"Strings = {string}, tipo {type(string)}")

    print('Posicion 0 ', numbers[0])

    # CRUD
    print("String ", string)
    print("Index = ", string.index('mundo'))
    print("Contar elementos existentes = ", string.count('harold'))

    lista = list(string)
    print(f"La nueva lista proveniente de una tupla = {lista}")
    lista[1] = 'Emmanuel'
    print('informacion final = ', lista)
    tupla = tuple(lista)
    print("Nueva tupla = ", tupla)
if __name__ == "__main__":
    tuplas()
