from alphabet import *
from plaintext import normalize
import sys

def encrypt(plaintext, key, table):
    if len(key) > 26:
        key = key[:26]

    plaintext = normalize(plaintext, ALPHABET)
    keyStream = toKeyStream(plaintext, key)
    tableAlphabet = "".join(table[0])
    ciphertext = ""

    for plaintextSymbol, keySymbol in zip(plaintext, keyStream):
        ciphertext += tableEncrypt(plaintextSymbol, keySymbol, tableAlphabet, table)
    
    return ciphertext

def decrypt(ciphertext, key, table):
    if len(key) > 26:
        key = key[:26]

    ciphertext = normalize(ciphertext, ALPHABET)
    keyStream = toKeyStream(ciphertext, key)
    tableAlphabet = "".join(table[0])
    plaintext = ""

    for ciphertextSymbol, keySymbol in zip(ciphertext, keyStream):
        plaintext += tableDecrypt(ciphertextSymbol, keySymbol, tableAlphabet, table)
    
    return plaintext

def generateTable(key):
    table = []
    keyAlphabet = generateKeyAlphabet(key)

    for offset in range(26):
        table.append(list(generateTableRow(keyAlphabet, offset)))
    
    return table

def loadTable(filePath):
    tableFile = open(filePath)
    table = []

    for row in tableFile:
        table.append(list(row))
    
    return table

def generateKeyAlphabet(key):
    alphabetMinusKey = ""

    for symbol in ALPHABET:
        if not symbol in key:
            alphabetMinusKey += symbol
    
    return key + alphabetMinusKey


def generateTableRow(keyAlphabet, offset):
    return keyAlphabet[offset:len(keyAlphabet)] + keyAlphabet[0:offset]

def toKeyStream(text, key):
    keyStream = ""
    keyIndex = 0

    for symbol in text:
        if keyIndex >= len(key):
            keyIndex = 0
            
        keyStream += key[keyIndex]
        keyIndex += 1
    
    return keyStream

def tableEncrypt(plaintextSymbol, keySymbol, tableAlphabet, table):
    return table[tableAlphabet.index(plaintextSymbol)][tableAlphabet.index(keySymbol)]

def tableDecrypt(ciphertextSymbol, keySymbol, tableAlphabet, table):
    return tableAlphabet[getTableRow(ciphertextSymbol, tableAlphabet.index(keySymbol), table)]

def getTableRow(targetSymbol, columnIndex, table):
    for row in range(len(table)):
        if table[row][columnIndex] == targetSymbol:
            return row
    
    return None

if __name__ == "__main__":
    if len(sys.argv) < 5:
        print("Usuage: -e/-d plaintext/ciphertext key pathToTableFile")
    else:
        table = loadTable(sys.argv[4])
        mode = sys.argv[1]

        if mode == "-e":
            print(encrypt(sys.argv[2], sys.argv[3], table))
        elif mode == "-d":
            print(decrypt(sys.argv[2], sys.argv[3], table))
