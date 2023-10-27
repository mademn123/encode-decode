# Nihitha Madem
def menu():
    print('Menu')
    print('-------------')
    print('1. Encode \n2. Decode \n3. Quit')
def encoder(password):
    password_new = ''
    for i in password:
        password_increment = int(i) + 3
        password_new += str(password_increment)
    return password_new

# Kaylee Pekar added this function.
def decode(password):
    decoded_password = ''
    for i in password:
        password_decrement = int(i) - 3
        decoded_password += str(password_decrement)
    return decoded_password

def main():
    game_continue = True
    while game_continue:
        menu()
        menu_option = int(input('Please enter an option: '))
        if menu_option == 1:
            choose_password = input('Please enter your password to encode: ')
            encoder(choose_password)
            print('Your password has been encoded and stored!')
        elif menu_option == 2:
            encoded_password = encoder(choose_password)
            decoded_password = decode(encoded_password)
            print(f'\nThe encoded password is {encoded_password}, and the original password is {decoded_password}')
        else:
            break
if __name__ == '__main__':
    main()



