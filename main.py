alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
symbol = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", " "]
number = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

go_again = 'yes'

while go_again == 'yes' or go_again == 'y':

    direction = input("Type 'encode' to encrypt and 'decode' to decrypt.\n").lower()
    text = input("Type your message.\n").lower()
    shift = int(input("Type the shift number:\n"))

    def cipher(original_text, shift_num):
        new_text = ""
        for letter in original_text:
            if direction == 'encode':
                if letter in alphabet:
                    new_index = alphabet.index(letter) + shift_num
                    new_index %= len(alphabet)
                    new_text += alphabet[new_index]
                elif letter in symbol:
                    new_index = symbol.index(letter) + shift_num
                    new_index %= len(symbol)
                    new_text += symbol[new_index]
                elif letter in number:
                    new_index = number.index(letter) + shift_num
                    new_index %= len(number)
                    new_text += number[new_index]
            elif direction == 'decode':
                if letter in alphabet:
                    new_index = alphabet.index(letter) - shift_num
                    new_index %= len(alphabet)
                    new_text += alphabet[new_index]
                elif letter in symbol:
                    new_index = symbol.index(letter) - shift_num
                    new_index %= len(symbol)
                    new_text += symbol[new_index]
                elif letter in number:
                    new_index = number.index(letter) - shift_num
                    new_index %= len(number)
                        #this returns the remaining number, if the inserted number is bigger than the alphabet length,
                        #so every time the insertedd number is within the range
                    new_text += number[new_index]
            else:
                print("Give valid input. Type 'encode' to encrypt and 'decode' to decrypt.")
                print("Try this time without using '' or leaving spaces between words.")

        print(f"Here is the {direction}d message: {new_text}")    
    
    cipher(text, shift)

    go_again = input("Do you want to use cipher again? If yes type 'yes' if no type 'no'.\n").lower()
    if go_again == 'no' or go_again == 'n':
        print("See you again soon!")
