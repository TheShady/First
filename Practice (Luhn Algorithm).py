# User Input
card_number = input('Enter card number(not real one): ')

# Clearing the input with translation table
card_translation = str.maketrans({'-': '', ' ': '', '.':'', '_': '', ',': ''})
translated_card_number = (card_number.translate(card_translation))

# Calculations
reversed_card_number = translated_card_number [::-1]
second_digits = reversed_card_number[1::2]
first_digits = reversed_card_number[::2]
sum_of_sdigits = 0
sum_of_fdigits = 0
for digit in second_digits:
    ddigit = int(digit) * 2
    if ddigit < 10:
        sum_of_sdigits += ddigit
    elif ddigit >= 10:
        sum_of_sdigits += ddigit//10 + ddigit%10
for digit in first_digits:
    sum_of_fdigits += int(digit)

# Final check
full_sum = sum_of_fdigits + sum_of_sdigits
if full_sum % 10 == 0:
    print('Valid')
else:
    print('Invalid')
