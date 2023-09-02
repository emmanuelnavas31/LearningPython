"""
    Los operadores logicos nos permiten realizar comparativas
"""


def logicos():
    # Operador and
    print(f'Operador AND (True and True): {True and True}')
    print(f'Operador AND (True and False): {True and False}')
    print(f'Operador AND (False and True): {False and True}')
    print(f'Operador AND (False and False): {False and False}')

    # Comparadores logicos con operadores
    print(f'10 > 5 y 5 < 10: {10 > 5 and 5 < 10}')
    print(f'10 > 5 y 5 > 10: {10 > 5 and 5 > 10}')

    stock = int(input("Ingrese un numero de stock: "))
    print(f'Stock: {stock >= 100 and stock <= 1000}')


   # Operador or
    print(f'Operador or (True or True): {True or True}')
    print(f'Operador or (True or False): {True or False}')
    print(f'Operador or (False or True): {False or True}')
    print(f'Operador or (False or False): {False or False}')

    role = input("Ingrese un rol: ")
    print(role == 'admin' or role == 'seller')

    # Operador logico NOT

    print(f'Operador not (True not True): {(not (True and True))}')
    print(f'Operadnot not (True not False): {(not (True and False))}')
    print(f'Operadnot not (False not True): {(not (False and True))}')
    print(f'Operadnot not (False not False): {(not (False and False))}')

    new_stock = int(input('Ingrese un nuevo stock'))
    print(f"Nuevo stock = {not (new_stock >= 100 and new_stock<= 1000)}")

if __name__ == '__main__':
    logicos()
