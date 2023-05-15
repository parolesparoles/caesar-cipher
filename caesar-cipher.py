alphabet = 'abcdefghijklmnopqrstuvwxyz'
print("Welcome to Python's Online Caesar Cipher Device!")
key = int(input("Please insert your key here: "))
newMessage = ' '
message = input("Please enter a character to message: ")
for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + key) % 26
        newCharacter = alphabet[newPosition]
        newMessage += newCharacter
    else:
        newMessage += character
print("Your new message is :", newMessage)
