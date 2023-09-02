def proyecto():
    user_option = input('Elija, Piedra, papel, tijera: ')
    computer_option = 'papel'

    if user_option == computer_option:
        print('Empate')

    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Piedra gana a tijera')
            print('User Gano')
        elif computer_option == 'papel':
            print('Papel gana a piedra')
            print('Computador gana')
        elif computer_option == 'tijera':
            print('Papel gana a piedra')
            print('Computador gana')

if __name__ == '__main__':
    proyecto()
