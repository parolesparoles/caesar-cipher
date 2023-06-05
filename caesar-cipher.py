import streamlit as st

st.title("Online Caesar Cipher Decipher Device")
st.text("Welcome to Python's Online Caesar Cipher Decipher Device!")
st.text("Do you wish to encrypt or decrypt your messages?")
alphabet = 'abcdefghijklmnopqrstuvwxyz'
newMessage = ' '
key = st.number_input("Please insert your key as an integer here: ", 0, 26)
message = st.text_input("Please enter a message: ")
if st.button("Encryption"):
  for character in message:
    if character in alphabet:
      position = alphabet.find(character)
      newPosition = (position + key)
      newCharacter = alphabet[newPosition]
      newMessage += newCharacter
    else:
      newMessage += character
      
if st.button("Decryption"):
  for character in message:
    if character in alphabet:
      position = alphabet.find(character)
      newPosition = (position - key) % 26
      newCharacter = alphabet[newPosition]
      newMessage += newCharacter
    else:
      newMessage += character

st.subheader("Your new message is:")
st.text(newMessage)
