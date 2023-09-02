def booleans():
    values = True
    print(f'Valores booleanos = {values} tipo de dato = {type(values)}')

    values = False
    print(f'Valores booleanos = {values} tipo de dato = {type(values)}')

    # Podemos utilizar operadores logicos para realizar la negacion del valor booleano

    new_values = not values
    print(f'Valores booleanos = {new_values} tipo de dato = {type(new_values)}')

    print(f'El valor es = {not True}')
    print(f"El valor es = {not False}")


if __name__ == '__main__':
    booleans()
