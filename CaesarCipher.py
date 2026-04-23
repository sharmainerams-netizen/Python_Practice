def lines():
    print('******************************************************************')

def caesar(text, shift, encrypt = True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    shift = shift % 26

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = - shift
    
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(alphabet + alphabet.upper(), shifted_alphabet + shifted_alphabet.upper())
    encrypted_text = text.translate(translation_table)
    return encrypted_text

def encrypt(text, shift):
    return caesar(text, shift)
    
def decrypt(text, shift):
    return caesar(text, shift, encrypt = False)

def user_input(choice):
    if choice == "A":
        text = input('Enter text: ')
        try:
            shift = int(input('Enter shift: '))
        except ValueError:
            return "Shift must be a number."
        return f"Encrypted text: {encrypt(text, shift)}"
    
    elif choice == "B":
        text = input('Enter text: ')
        try:
            shift = int(input('Enter shift: '))
        except ValueError:
            return "Shift must be a number."
        return f"Decrypted text: {decrypt(text, shift)}"
    
    else:
        return "Invalid input: type A, B, or C"

while True:

    lines()
    print('\nA: Encode \nB: Decode \nC: Exit')
    choice = input().upper()
    
    if choice == "C":
        break
    
    print(user_input(choice))