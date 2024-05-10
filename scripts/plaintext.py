def normalize(text, alphabet):
    text = text.lower()
    plaintext = ""

    for symbol in text:
        if symbol.lower() in alphabet:
            plaintext += symbol
    
    return plaintext