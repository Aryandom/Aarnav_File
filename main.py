from decode import decode
from encode import encode


def main():
    text = '''Menu
-------------
1. Encode
2. Decode
3. Quit

Please enter an option: '''
    pw = ''
    while True:
        option = int(input(text))
        if option == 1:
            password = str(input('Please enter your password to encode: '))
            pw = encode(password)
            print('Your password has been encoded and stored!')
        elif option == 2:
            print(f'The encoded password is {pw}, and the original password is {decode(pw)}.')
        elif option == 3:
            break


if __name__ == '__main__':
    main()
