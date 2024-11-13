def shift_char(char, key, direction):
    if 'a' <= char <= 'z':  # Lowercase characters
        base = ord('a')
        offset = (ord(char) - base + direction * key) % 26
        return chr(base + offset)
    elif 'A' <= char <= 'Z':  # Uppercase characters
        base = ord('A')
        offset = (ord(char) - base + direction * key) % 26
        return chr(base + offset)
    else:
        return char  # Non-alphabet characters are not shifted

def caesar_cipher(text, key, encrypt=True):
    direction = 1 if encrypt else -1
    shifted_text = ''.join(shift_char(char, key, direction) for char in text)
    return shifted_text

def main():
    text = input("Enter text: ")
    choice = input("(E)ncrypt or (D)ecrypt? ").upper()
    key = int(input("Enter the number of positions: "))
    
    if choice == "E":
        result = caesar_cipher(text, key, encrypt=True)
    elif choice == "D":
        result = caesar_cipher(text, key, encrypt=False)
    else:
        print("Invalid choice. Please enter 'E' for encrypt or 'D' for decrypt.")
        return  # Exit main function if choice is invalid
    
    print("Result:", result)

main()
