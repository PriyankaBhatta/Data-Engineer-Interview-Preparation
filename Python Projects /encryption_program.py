import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"chars: {chars}")
print(f"keys: {key}")

#ENCRYPT
plain_text = input("Enter a message to encrypt: ")
cipher_test = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_test += key[index]

print(f"Original Message: {plain_text}")
print(f"Encrypted Message: {cipher_test}")

#DECRYPT
cipher_test = input("Enter a message to decrypt: ")
plain_text = ""

for letter in cipher_test:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Encrypted Message: {plain_text}")
print(f"Original Message: {cipher_test}")
