# Cryptography Challenge #1 - www.101computing.net/cryptography-challenge-1/

# For this challenge, we are giving you a piece of Python code use to encrypt a message.
# Your first task is to reverse-engineer this code to understand how this encryption algorithm works.
# Then, your challenge consists of writing a new function called decrypt(),
# that takes two parameters (a ciphertext and a key) and returns the plaintext corresponding to the given ciphertext.


import random, time


# A basic encryption algorithm...
def encrypt(plaintext, key):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ciphertext = ""
    for i in range(0, len(plaintext)):
        character = plaintext[i]
        ciphertext = ciphertext + character
        for j in range(0, key):
            ciphertext = ciphertext + random.choice(alphabet)
    return ciphertext


# Main program starts here...
# Input...
plaintext = input("Enter a message to encrypt (plaintext)")
key = int(input("Input a key as a number between 1 and 10"))
while not (1 <= key <= 10):
    print("Invalid key, try again!")
    key = int(input("Input a key as a number between 1 and 10"))

# Process...
print("...")
time.sleep(1)
print("Encrypting plaintext...")
time.sleep(1)
print("...")
time.sleep(1)
ciphertext = encrypt(plaintext, key)

# Output...
print("Ciphertext:")
print(ciphertext)
