from alphabet import *
from plaintext import normalize

def encrypt(plaintext, key):
    if len(key) > 26:
        key = key[:26]

    plaintext = normalize(plaintext, ALPHABET)
    table = generatePlainTextTable(plaintext, key)
    tableTranspose = transpose(table, key)
    tableTransformed = transform(tableTranspose, key)

    cipherText = ""

    for row in tableTransformed:
        cipherText += "".join(row)

    return cipherText

def decrypt(ciphertext, key):
    if len(key) > 26:
        key = key[:26]

    ciphertext = normalize(ciphertext, ALPHABET)

    return ciphertext

def generatePlainTextTable(plaintext, key):
    table = []
    row = []

    for symbolIndex in range(len(plaintext) + 1):
        if len(row) == len(key) or symbolIndex == len(plaintext):
            table.append(row)
            row = []
        else:
            row.append(plaintext[symbolIndex])
    
    return table

def transpose(table, key):
    if len(table[0]) != len(key):
        return None
    
    transposedTable = []

    for column in range(len(key)):
        transposedTable.append(getColumn(table, column))

    return transposedTable

def transform(table, key):
    keyList = list(key)
    keyList.sort(key=lambda symbol: ALPHA_OFFSETS[symbol])

    transformedTable = []

    for symbol in keyList:
        transformedTable.append(table[key.index(symbol)])

    return transformedTable

def getColumn(table, columnIndex):
    column = []

    for i in range(len(table)):
        if columnIndex < len(table[i]):
            column += table[i][columnIndex]
    
    return column