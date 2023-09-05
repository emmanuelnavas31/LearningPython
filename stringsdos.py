def strings():
    text = 'El sabe programar en PYTHON'
    print('JavaScript' in text)
    print('python' in text)

    if 'python' in text:
        print('Elegiste bien')
    else:
        print('Que bien')

    # Evaluacion del tamano o cantidad de caracteres
    # Funcion LEN()
    size = len(text)
    print('Caracteres contenidos en el texto: ', size)

    #
    print('Cambio de texto a mayusculas: ', text)
    print('Cambio de texto a mayusculas: ', text.upper())
    print('Cambio de texto a minusculas: ', text.lower())
    print('Cuantas veces existe una a: ', text.count('a'))
    print('Lo mayuscula a minuscula y viseversa: ', text.swapcase())
    print('Respuesta booleana: ', text.startswith('El'))
    print('Respuesta booleana: ', text.endswith('scipt'))
    print('Reemplazar: ', text.replace('PYTHON', 'JAVA'))

    texto2 = 'este es un titulo de repaso'
    print('Colocar el primer caracter en mayuscula ', texto2.capitalize())
    print('Funcion de titulo', texto2.title())
    print('Funcion de digito', texto2.isdigit())
    print('Funcion si es digito', "123".isdigit())


if __name__ == '__main__':
    strings()
