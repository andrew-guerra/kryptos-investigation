from math import sqrt

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

ALPHA_OFFSETS = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": 3,
    "e": 4,
    "f": 5,
    "g": 6,
    "h": 7,
    "i": 8,
    "j": 9,
    "k": 10,
    "l": 11,
    "m": 12,
    "n": 13,
    "o": 14,
    "p": 15,
    "q": 16,
    "r": 17,
    "s": 18,
    "t": 19,
    "u": 20,
    "v": 21,
    "w": 22,
    "x": 23,
    "y": 24,
    "z": 25,
}

LETTER_FREQUENCY = {
    "a": 0.082,
    "b": 0.015,
    "c": 0.028,
    "d": 0.043,
    "e": 0.127,
    "f": 0.022,
    "g": 0.02,
    "h": 0.061,
    "i": 0.07,
    "j": 0.0015,
    "k": 0.0077,
    "l": 0.04,
    "m": 0.024,
    "n": 0.067,
    "o": 0.075,
    "p": 0.019,
    "q": 0.00095,
    "r": 0.06,
    "s": 0.063,
    "t": 0.091,
    "u": 0.028,
    "v": 0.0098,
    "w": 0.024,
    "x": 0.0015,
    "y": 0.02,
    "z": 0.00074,
}

LETTER_FREQUENCY_NORMALIZED = {
    "a": 0.3200628410583757, 
    "b": 0.05854808068141018, 
    "c": 0.10928975060529901, 
    "d": 0.16783783128670918, 
    "e": 0.49570708310260625, 
    "f": 0.08587051833273493, 
    "g": 0.07806410757521358, 
    "h": 0.2380955281044014, 
    "i": 0.27322437651324755, 
    "j": 0.005854808068141018, 
    "k": 0.03005468141645723, 
    "l": 0.15612821515042716, 
    "m": 0.0936769290902563, 
    "n": 0.2615147603769655, 
    "o": 0.29274040340705093, 
    "p": 0.0741609021964529, 
    "q": 0.003708045109822645, 
    "r": 0.23419232272564072, 
    "s": 0.24590193886192277, 
    "t": 0.3551916894672218, 
    "u": 0.10928975060529901, 
    "v": 0.03825141271185465, 
    "w": 0.0936769290902563, 
    "x": 0.005854808068141018, 
    "y": 0.07806410757521358, 
    "z": 0.0028883719802829024
}

def generateLetterFrequencyVector(text):
    frequencyVector = generateEmptyLetterFrequencyVector()

    for symbol in text:
        frequencyVector[symbol] += 1

    for symbol in ALPHABET:
        frequencyVector[symbol]
    
    return normalize(frequencyVector)

def generateEmptyLetterFrequencyVector():
    frequencyVector = {}
    for symbol in ALPHABET:
        frequencyVector[symbol] = 0
    
    return frequencyVector

def normalize(vec):
    noramlizedVector = {}
    len = length(vec)

    for symbol, frequency in vec.items():
        noramlizedVector[symbol] = frequency / len
    
    return noramlizedVector

def compare(vec1, vec2):
    return dotProduct(vec1, vec2)

def isSimilar(vec1, vec2, threshold=0.9):
    return dotProduct(vec1, vec2) >= threshold

def dotProduct(vec1, vec2):
    dotProduct = 0
    for symbol in ALPHABET:
        dotProduct += vec1[symbol] * vec2[symbol]
    
    return dotProduct

def length(vec):
    return sqrt(dotProduct(vec, vec))