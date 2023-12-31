# User Inputs
input_message = input('Enter the message you want to modify: ')
key_word = input('Enter the key for encryption or decryption: ')
alphabet = input('Enter custom alphabet (optional): ')
mode = int(input('Choose mode: 1 to encode, -1 to decode: '))

# Encode/Decode function
def vigenere (input_message, key_word, mode = 1, alphabet ='abcdefghijklmnopqrstuvwxyz'):
    output_message = ''
    current_key = 0
    for char in input_message.lower():
        char_index = alphabet.find(char)
        key_char_index = (alphabet.find(key_word[current_key]))
        new_index = (char_index + key_char_index * mode)%26
        current_key += 1
        output_message += alphabet[new_index]

    print (output_message)


# Checks if there is custom alphabet input
if alphabet == '':
    vigenere(input_message,key_word,mode)
else:
    vigenere(input_message,key_word,mode,alphabet)