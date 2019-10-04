# Affine Cipher
# http://inventwithpython.com/hacking (BSD Licensed)
# 仿射加密法

import sys, pyperclip, cryptomath, random

# 符号集，可加密的字符集
SYMBOLS = """ !"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~""" # note the space at the front


def main():
    # 待加密字符串
    myMessage = """"A computer would deserve to be called intelligent if it could deceive a human into believing that it was human." -Alan Turing"""
    
    myKey = 2023  # 密钥
    
    myMode = 'encrypt' # set to 'encrypt' or 'decrypt'

    if myMode == 'encrypt':
        translated = encryptMessage(myKey, myMessage)
    elif myMode == 'decrypt':
        translated = decryptMessage(myKey, myMessage)
    print('Key: %s' % (myKey))
    print('%sed text:' % (myMode.title()))  # str.title()方法返回标题化的字符串
    print(translated)
    pyperclip.copy(translated)
    print('Full %sed text copied to clipboard.' % (myMode))

# 将密钥进行分解，乘法密钥 A，加法密钥 B
def getKeyParts(key):
    keyA = key // len(SYMBOLS)
    keyB = key % len(SYMBOLS)
    return (keyA, keyB)


def checkKeys(keyA, keyB, mode):
    if keyA == 1 and mode == 'encrypt':
        sys.exit('The affine cipher becomes incredibly weak when key A is set to 1. Choose a different key.')
    if keyB == 0 and mode == 'encrypt':
        sys.exit('The affine cipher becomes incredibly weak when key B is set to 0. Choose a different key.')
    if keyA < 0 or keyB < 0 or keyB > len(SYMBOLS) - 1:
        sys.exit('Key A must be greater than 0 and Key B must be between 0 and %s.' % (len(SYMBOLS) - 1))
    # 乘法密钥必须与字符集大小互质，否则会出现不同字符加密后是同一个字符的现象
    if cryptomath.gcd(keyA, len(SYMBOLS)) != 1:
        sys.exit('Key A (%s) and the symbol set size (%s) are not relatively prime. Choose a different key.' % (keyA, len(SYMBOLS)))

# 加密算法：cipherindex = (plainindex * KeyA + KeyB) mod len(SYMBOLS)
def encryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'encrypt')
    ciphertext = ''
    for symbol in message:
        if symbol in SYMBOLS:
            # encrypt this symbol
            symIndex = SYMBOLS.find(symbol)
            ciphertext += SYMBOLS[(symIndex * keyA + keyB) % len(SYMBOLS)]
        else:
            ciphertext += symbol # just append this symbol unencrypted
    return ciphertext

# 解密需要用到乘法密钥 A 的模逆，解密算法为 plainindex = (cipherindex * modInverseOfKeyA) mod len(SYMBOLS)
# cipherindex为密文在可加密字符集里面的索引
def decryptMessage(key, message):
    keyA, keyB = getKeyParts(key)
    checkKeys(keyA, keyB, 'decrypt')
    plaintext = ''
    modInverseOfKeyA = cryptomath.findModInverse(keyA, len(SYMBOLS))

    for symbol in message:
        if symbol in SYMBOLS:
            # decrypt this symbol
            symIndex = SYMBOLS.find(symbol)
            plaintext += SYMBOLS[(symIndex - keyB) * modInverseOfKeyA % len(SYMBOLS)]
        else:
            plaintext += symbol # just append this symbol undecrypted
    return plaintext

# 创建随机密钥，伪随机
def getRandomKey():
    while True:
        keyA = random.randint(2, len(SYMBOLS))
        keyB = random.randint(2, len(SYMBOLS))
        if cryptomath.gcd(keyA, len(SYMBOLS)) == 1:
            return keyA * len(SYMBOLS) + keyB


# If affineCipher.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()