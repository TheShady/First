def convert_to_snake_cased(input_string):
    snake_cased_char_list = [
        '_' + char.lower() if char.isupper()
        else char
        for char in input_string
    ]
    return ''.join(snake_cased_char_list)


def main():
    print(convert_to_snake_cased(input('Enter your string to convert: ')).strip('_'))


if __name__ == '__main__':
    main()
