ALPHABET_SIZE = 26

#Getting the user inputs(message and key) and storing them in variables
message: str = input("Message: ")  
key: int = int(input("Key: "))

# Creating an empty string to store the ciphertext
ciphertext: str = ""


for letter in message: 

        # Checking whether the character is a letter and if it is uppercase or lowercase, then shifting the letter by the key value and wrapping around if necessary
        if  "A" <= letter <= "Z":  
            shifted = ord(letter) + key # Converting the letter to its ASCII value and adding the key 
            if shifted > ord("Z"): # Checking if the shifted value exceeds the ASCII value of 'Z'
                shifted -= ALPHABET_SIZE # Subtracting the size of the alphabet to wrap around
            ciphertext += chr(shifted) # Converting back to the word and adding it to the ciphertext string

        elif "a" <= letter <= "z":
            shifted = ord(letter) + key 
            if shifted > ord("z"): # Checking if the shifted value exceeds the ASCII value of 'z'
                shifted -= ALPHABET_SIZE 
            ciphertext += chr(shifted) 
             
        else:
             ciphertext += letter # non_letter characters are keeping the same in the ciphertext

print("Ciphertext: ", ciphertext)

plaintext = ""


for letter in ciphertext:
    if "A" <= letter <= "Z":
        shifted = ord(letter) - key # Converting the letter to its ASCII value and subtracting the key
        if shifted < ord("A"): # Checking if the shifted value is less than the ASCII value of 'A'
            shifted += ALPHABET_SIZE # Adding the alphabet size
        plaintext += chr(shifted) # Converting back to the word and adding it to the plaintext 

    elif "a" <= letter <= "z":
        shifted = ord(letter) - key
        if shifted < ord("a"): # Checking if the shifted value is less than the ASCII value of 'a'
            shifted += ALPHABET_SIZE
        plaintext += chr(shifted)
    else:
        plaintext += letter # non_letter characters are keeping the same in the plaintext

print("Plaintext: ", plaintext)


assert message == plaintext, "The encryption-decryption loop doesn't close. " # Checking whether the original message and the decrypted plaintext are the same and if not it raises an assertion error with a message