letters =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caeser(text, shift_value, dir):
    text_as_list = list(text.lower())

    encoded_list = []
    for i in text_as_list:
        if i not in letters:
            encoded_list.append(i)
        else:
            if dir == "encode":
                shifted_letter_index = letters.index(i) + shift_value
            if dir == "decode":
                shifted_letter_index = letters.index(i) - shift_value
            encoded_list.append(letters[shifted_letter_index % 26])

    encoded_text = "".join(encoded_list)
    print(f"The {dir}d value is: {encoded_text}")

should_continue = True

while should_continue:
    direction = input("Enter 'encode' to encrypt and 'decode' to decrypt: ").lower()
    original_text = str(input("Enter the text to be processed: "))
    shift_to = int(input("Enter the shift value: "))

    #caeser(dir = direction, text = original_text, shift_value = shift_to)
    caeser(original_text, shift_to, direction)

    repeat = input("Would you like to continue? Type yes or no: ").lower()
    if repeat == "no":
        print("Goodbye!")
        should_continue = False