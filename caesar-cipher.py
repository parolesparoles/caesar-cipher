import streamlit as st

st.title("Online Caesar Cipher Decipher Device")
st.text("Welcome to Python's Online Caesar Cipher Decipher Device!")
yes_no = st.text_input("Do you wish to encrypt or decrypt your messages? (Press 1 for encryption, press 2 for decryption)")
alphabet = 'abcdefghijklmnopqrstuvwxyz'
newMessage = ' '

if yes_no == "1":
  key = st.text_input(int("Please insert your key as an integer here: "))
  message = st.text_input("Please enter a message to encrypt: ")
  for character in message:
    if character in alphabet:
      position = alphabet.find(character)
      newPosition = (position + key)
      newCharacter = alphabet[newPosition]
      newMessage += newCharacter
    else:
      newMessage += character
elif yes_no == "2":
  key = st.text_input("Please insert your key as an integer here: ")
  key = int(key)
  message = st.text_input("Please enter a message to decrypt: ")
  for character in message:
    if character in alphabet:
      position = alphabet.find(character)
      newPosition = (position - key) % 26
      newCharacter = alphabet[newPosition]
      newMessage += newCharacter
    else:
      newMessage += character
else:
  st.text("Error detected. Please refresh the page and try again.")
encryption_decryption()
st.text(newMessage)
