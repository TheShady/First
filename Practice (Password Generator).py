import string
import re
import secrets

# User input
length = input('Enter the length of password (8 by default): ')
if length == '':
    length = 8

# Alphabet
all_chars = string.ascii_letters + string.digits + string.punctuation

# Generator
def generate_password(length,nums = 2,uppercase = 2,lowercase = 2, sp_char = 1):
    constrains = [
        (nums, '[0-9]'),
        (uppercase, '[A-Z]'),
        (lowercase, '[a-z]'),
        (sp_char, '[string.punctuation]')
    ]
    while True:
        password = ''
        for _ in range(int(length)):
            password += secrets.choice(all_chars)
        if all(
            len(re.findall(pattern, password)) >= constraint for constraint, pattern in constrains
        ):
            break
    return password

if __name__ == '__main__':
    print(generate_password(length))

