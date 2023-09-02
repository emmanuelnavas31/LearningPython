'''
    Valores string son cadenas de caracteres los cuales nos permiten definir nombres  a parte de que nos permiten
    concatenar informacion general entre otros procesos, nosotros podemos realizar la asignacion directa del tipo de
    dato o tamnbien podemos realizar el cambio de tipo de variable en cualquier punto que deseemos usando la siguiente
    nomenclatura.

    • str

    las concatenaciones las podemos realizar con el simbolo mas.
'''


def string():
    name = str(input('Por favor ingrese su nombre: '))
    last_name = str(input('Por favor ingrese su apellido: '))
    full_name = (name + ' ' + last_name)
    print(f'La informacion del usuario es: {full_name}')

    age = int(input('Ingrese su edad: '))
    # Manejo de apostrofes en las cadenas de caracteres, para ello usamos comillas dobles mas no sencillas
    quote = "Hello, I'm Backend Developer"
    print(f'Agregando un apostrofe a mis cadenas de caracteres string: {quote}')

    # Tambien podemos realizarlo de forma inversa, encerrando el texto en comilla sencilla e internamente usar comillas dobles
    quote2 = 'Hello "Mundo" '
    print(f'Comillas sencillas : {quote2}')

    # Manejo de formatos

    formato1 = "Hola mi nombre es " + name + " mi apellido es " + last_name + " y soy desarrollador Backend"
    print('formato 1 = ', formato1)

    formato2 = f"Hola mi nombre es {name} mi apellido es {last_name} y soy desarrollador Backend"
    print('formato 2 = ', formato2)

    formato3 = "Hola mi nombre es {} y mi apellido es {}".format(name, last_name)
    print('formato 3 = ', formato3)

    final = "Hola mi nombre es {}, mi apellido es {} y mi edad es {}, y tengo 3 years siendo programador full stack".format(
        name, last_name, age)
    print(final)
    

if __name__ == '__main__':
    string()
