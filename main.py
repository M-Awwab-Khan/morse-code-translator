from mapping import morse_code_dict


while True:
    choice = int(input('Type 1 to translate text to morse code.\nType 2 to translate morse code to text.\nType q to exit.\n'))
    if choice == 1:
        user_input = input('Enter the text: ')
        translated = ''
        for char in user_input.strip():
            translated += morse_code_dict[char.upper()]


        print(translated)