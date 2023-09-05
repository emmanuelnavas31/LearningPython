def indexingSlicing():
    text = 'El equipo de programacion'
    """
        Nosotros podemos acceder a las posiciones
        del texto.
    """
    print("Texto = ", text[0])
    print("Texto = ", text[1])
    longitud = len(text)
    print("Texto = ", text[longitud-1])
    print("Texto = ", text[-1])

    """
        Slicing: 
    """
    print("Texto = ", text[3:10])
    print("Texto = ", text[:10])
    print("Texto = ", text[5:-1])
    print("Texto = ", text[5:])
    print("Texto = ", text[:])
    print("Texto = ", text[:16:2]) # Saltos


if __name__ == '__main__':
    indexingSlicing()
