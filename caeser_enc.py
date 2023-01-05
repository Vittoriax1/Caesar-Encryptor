def caesar_cipher(plaintext, shift):
    # Create a blank result string
    result = ""

    # Iterate over each character in the plaintext
    for char in plaintext:
        # If the character is a letter, shift it by the specified number of positions
        if char.isalpha():
            # Get the ASCII value of the character
            ascii_value = ord(char)

            # Shift the ASCII value by the specified number of positions
            if char.isupper():
                ascii_value = (ascii_value - 65 + shift) % 26 + 65
            else:
                ascii_value = (ascii_value - 97 + shift) % 26 + 97

            # Convert the shifted ASCII value back to a character and add it to the result
            result += chr(ascii_value)
        # If the character is not a letter, just add it to the result
        else:
            result += char

    # Return the result
    return result

# Get the user's plaintext and shift
plaintext = input("Enter the plaintext: ")
shift = int(input("Enter the shift: "))

# Encrypt the plaintext using the Caesar cipher
ciphertext = caesar_cipher(plaintext, shift)

# Print the ciphertext
print("Ciphertext:", ciphertext)
