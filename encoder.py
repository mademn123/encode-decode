def encoder(password):
    password_new = ''
    for i in password:
        password_increment = int(i) + 3
        password_new += str(password_increment)
    print(password_new)
    return password_new
def main():
    print('Menu')
    print('-------------')
    print('1. Encode \n2. Decode \n3. Quit')
    menu_option = int(input('Please enter an option: '))
    game_continue = True
    while game_continue:
        if menu_option == 1:
            choose_password = input('Please enter your password to encode: ')
            encoder(choose_password)
            print('Your password has been encoded and stored!')
        elif menu_option == 2:
            pass
        else:
            break
if __name__ == '__main__':
    main()