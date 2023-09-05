import random


def proyecto():
    options = ('piedra', 'papel', 'tijera')
    user_option = input('Elija, Piedra, papel, tijera: ').lower()
    if not user_option in options:
        print('La opcion no es valida.')
    print('INformacion = ', user_option)
    computer_option = random.choice(options)

    print('Opcion del usuario = ', user_option)
    print('Opcion de la computadora = ', computer_option)
    if user_option == computer_option:
        print('Empate')

    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Piedra gana a tijera')
            print('User Gano')
        else:
            print('Papel gana a piedra')
            print('Computador gana')
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('Papel gana a piedra')
            print('Usuario gana')
        else:
            print('Tijera gana a papel')
            print('Computador gana')
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('Tijera gana papel')
            print('Usuario gana')
        else:
            print('Piedra gana tijera')
            print('Computador gana')


if __name__ == '__main__':
    proyecto()
