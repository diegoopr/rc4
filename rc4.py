
from pydoc import plain


def asciiToInt(text):
    ascii = list(text.encode('ascii'))
    return ascii


def intToAscii(list):
    plain = "".join(chr(i) for i in list)
    return plain


def decToHex(list):
    hexa = ""
    for i in list:
        hexa += hex(i)[2:]

    return hexa


def KSA(key):
    j = 0
    #n = 2 ** 8 #modificar el 8 por la cantidad de bytes que se quieran usar
    #por default es 2 a la 8 para tener los 256 que originalmente tiene el algoritmo
    S = [i for i in range(256)]
    asciiKey = asciiToInt(key)
    keyLen = len(asciiKey)

    for i in range(256):
        j = (j + S[i] + asciiKey[i % keyLen]) % 256;
        S[i], S[j] = S[j], S[i]
    
    return S


def PRGA(S, messageLen):
    i = j = 0
    keyStream = []

    for i in range(messageLen):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        t = (S[i] + S[j]) % 256
        keyStream.append(S[t])
    
    print(decToHex(keyStream))
    return keyStream
    

def xor(message, keyStream):
    xored = []
    for i in range(len(message)):
        new = keyStream[i] ^ message[i]
        xored.append(new)
    
    return xored
    

def encrypt(key, plain):
    message = asciiToInt(plain)
    keyStream = PRGA(KSA(key), len(message))
    encrypted = xor(keyStream, message)

    return decToHex(encrypted) 


"""---------Driver Program---------"""
key1 = "Key"
plaintext1 = "Plaintext"
key2 = "Wiki"
plaintext2 = "pedia"
key3 = "Secret"
plaintext3 = "Attack"
print(key1)
print(plaintext1)
print(encrypt(key1, plaintext1))