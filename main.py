from mapping import morse_code_dict

user_input = input('Enter any text to translate: ')
translated = ''
for char in user_input.strip():
    translated += morse_code_dict[char.upper()]


print(translated)