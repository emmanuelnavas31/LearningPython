def diccionarios():
    diccionario = {}
    print("Diccionario = ", diccionario, type(diccionario))

    diccionario = {
        'nombre': 'Harold',
        'apellido': 'Navas',
        'profesion': 'Desarrollador full Stack',
        'experiencia': 5,
        'edad': 27,
        'skill': ['Python', 'JavaScript', 'Django']
    }
    print("Diccionario = ", diccionario, type(diccionario))
    print("Elementos = ", len(diccionario))
    print(f"Accedemos a una llave nombre {diccionario['nombre']}")
    # De la siguiente manera podemos acceder a una llave, pero en caso de que esta
    # no llegue a exitir nos va a devolver un none sin que se optenga un error de la misma
    print(f"Dict con valor none: {diccionario.get('pruebas')}")
    print(f"Accedemos a una llave nombre {diccionario.get('nombre')}")
    # Validemos si exite alguna informacion
    print('profesion' in diccionario)
    print('noexiste' in diccionario)

    # Procesos de actualizacion e insercion en un diccionario
    diccionario['nombre'] = 'Emmanuel'
    print(f"Nuevo diccionario = {diccionario}")
    diccionario['edad'] -= 10
    print(f"Nuevo diccionario edad = {diccionario}")
    diccionario['skill'].append('Ruby')
    print(f"Nuevo diccionario skill = {diccionario}")

    # Metodos de eliminacion
    del diccionario['apellido']
    print(f"Eliminando apellido: {diccionario}")
    diccionario.pop('profesion')
    print(f"Eliminando profesion: {diccionario}")

    # acceder a los items de un diccionario y sus valores
    print(f"Keys: {diccionario.keys()}")
    print(f"Valores: {diccionario.values()}")


if __name__ == '__main__':
    diccionarios()
