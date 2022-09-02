def decrypt(ciphertext: str, key: int) -> str:
    decrypted = ""
    for i in range(0, int(len(ciphertext)/(key + 1))):
        decrypted = decrypted + ciphertext[i * (key + 1)]
    return decrypted

