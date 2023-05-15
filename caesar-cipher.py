import streamlit as st

st.title("Online Caesar Cipher Decipher Device")
st.text("Welcome to Python's Online Caesar Cipher Decipher Device!")
yes_no = st.text_input("Do you wish to encrypt or decrypt your messages? (Encrypt/Decrypt)")
alphabet = 'abcdefghijklmnopqrstuvwxyz'

if yes_no == "Encrypt":

  key = st.text_input("Please insert your key here: ")

newMessage = ' '
message = input("Please enter a message to encrypt: ")
for character in message:
    if character in alphabet:
        position = alphabet.find(character)
        newPosition = (position + key) % 26
        newCharacter = alphabet[newPosition]
        newMessage += newCharacter
    else:
        newMessage += character

 
