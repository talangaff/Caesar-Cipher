lowercaseAlphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
uppercaseAlphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

def main():
    while True:
        try:
            command = input("Input a command (encrypt, decrypt, decryptWithoutKey, or exit): ").lower().strip()

            if command == "encrypt":
                text = input("Input the text to encrypt: ")
                key = int(input("Input the encryption key: "))

                print(encrypt(text, key))

            elif command == "decrypt":
                text = input("Input the text to decrypt: ")
                key = int(input("Input the decryption key: "))
               
                print(decrypt(text, key))

            elif command == "decryptwithoutkey":
                text = input("Input the text to decrypt: ")

                print(decryptWithoutKey(text))

            elif command == "exit":
                break
            
            else:
                print("Invalid command")

        except Exception as err:
            print(err)
    

def encrypt(plaintext, key):
    plaintext = str(plaintext)
    newLower = lowercaseAlphabet[:]
    newUpper = uppercaseAlphabet[:]

    key %= 26

    while key > 0:
        key -= 1
        letter = newLower.pop(0)
        newLower.append(letter)
        letter = newUpper.pop(0)
        newUpper.append(letter)

    newText = ""

    for letter in plaintext:
        if letter in lowercaseAlphabet:
            newText += newLower[lowercaseAlphabet.index(letter)]
        elif letter in uppercaseAlphabet:
            newText += newUpper[uppercaseAlphabet.index(letter)]
        else:
            newText += letter
    
    return newText

def decrypt(ciphertext, key):
    return encrypt(ciphertext, 26-key)

def decryptWithoutKey(ciphertext):
    list = []
    
    for possibleKey in range(26,0,-1):
        list.append(encrypt(ciphertext, possibleKey))
    
    return list

if __name__ == "__main__":
    main()
