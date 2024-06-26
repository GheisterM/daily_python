import art, os
alphabet = [x for x in 'abcdefghijklmnopqrstuvwxyz']
actions = ("encode", "decode")

def caesar(text, shift, action):
    message = ""
    shift = shift % len(alphabet)
    for char in text:
        if char in alphabet:
            newChar = alphabet.index(char) + shift if action == 'encode' else alphabet.index(char) - shift
            if newChar >= len(alphabet):
                newChar -= len(alphabet)
            message = message + alphabet[newChar]
        else:
            message = message + char

    print(f"The {action}d text is {message}")

if __name__ == '__main__':
    print(art.logo)
    cont_code = "yes"
    while cont_code == "yes":
        direction = ""
        valid_direction = False
        while not valid_direction:
            direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
            if direction in actions:
                valid_direction = True

        plain_text = input("Type your message:\n").lower()

        shift_amount = 0
        shift_ready = False
        while not shift_ready:
            shift_text = input("Type the shift number:\n")
            shift_ready = True
            try:
                shift_amount = int(shift_text)
            except:
                print("Invalid value, please try again.")
                shift_ready = False

        caesar(text=plain_text, shift=shift_amount, action=direction)

        cont_code = ""
        while cont_code not in ("yes", "no"):
            cont_code = input("Do you want to continue encrypting/decrypting? (yes/no)\n").lower()
            if(cont_code == "yes"): 
                if os.name == 'nt': 
                    os.system('cls')
                else:
                    os.system('clear')
            
    print("Goodbye!")