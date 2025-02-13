# RSA Cipher
# http://inventwithpython.com/hacking (BSD Licensed)

import sys
import base64

# IMPORTANT: The block size MUST be less than or equal to the key size!
# (Note: The block size is in bytes, the key size is in bits. There
# are 8 bits in 1 byte.)
DEFAULT_BLOCK_SIZE = 128 # 128 bytes
BYTE_SIZE = 256 # One byte has 256 different values.

def main():
    # Runs a test that encrypts a message to a file or decrypts a message
    # from a file.
    filename = 'encrypted_file.txt' # the file to write to/read from
    
    
    mode = 'encrypt' # set to 'encrypt' or 'decrypt'
    # mode = 'decrypt'

    if mode == 'encrypt':
        # message = 'My name is Ye Shan, nice to meet you !'
        # message = '''"Journalists belong in the gutter because that is where the ruling classes throw their guilty secrets." -Gerald Priestland "The Founding Fathers gave the free press the protection it must have to bare the secrets of government and inform the people." -Hugo Black'''
        
        with open(filename, "rb") as f:  #二进制格式读取
            base64_data = base64.b64encode(f.read())  #使用base64进行编码
            # print(base64_data)
            file = open('img.txt','wt')  #写成文本格式
            file.write(base64_data.decode('utf-8'))  # bytes.decode(‘utf-8’)
            file.close()

        # 图像流测试
        with open('img.txt', 'r') as f:
            message = f.read()

        pubKeyFilename = 'al_sweigart_pubkey.txt'
        print('Encrypting and writing to %s...' % (filename))
        
        import time
        start = time.perf_counter()
        encryptedText = encryptAndWriteToFile(filename, pubKeyFilename, message)
        end = time.perf_counter()
        

        print('Encrypted text:')
        print(encryptedText)

        print('done !')
        print(f'Cost {end-start} seconds')

    elif mode == 'decrypt':
        privKeyFilename = 'al_sweigart_privkey.txt'
        print('Reading from %s and decrypting...' % (filename))

        from time import perf_counter
        start = perf_counter()
        decryptedText = readFromFileAndDecrypt(filename, privKeyFilename)
        end = perf_counter()
        

        print('Decrypted text:')
        print(decryptedText)

        # 将解码结果写到文件中
        with open('decrypted_file.txt', 'w') as f:
            f.write(decryptedText)
        
        # 解码，Base64 to image
        with open('decrypted_file.txt', "r") as f:
            imgdata = base64.b64decode(f.read())
            file = open('new.jpg','wb')
            file.write(imgdata)  # str.encode(‘utf-8’) 
            file.close()

        print(f'Cost {end-start} seconds')

def getBlocksFromText(message, blockSize=DEFAULT_BLOCK_SIZE):
    # Converts a string message to a list of block integers. Each integer
    # represents 128 (or whatever blockSize is set to) string characters.

    messageBytes = message.encode('ascii') # convert the string to bytes

    blockInts = []
    for blockStart in range(0, len(messageBytes), blockSize):
        # 对messageBytes划分区块，blockSize个英文字符（字节）为一个区块
        blockInt = 0
        for i in range(blockStart, min(blockStart + blockSize, len(messageBytes))):
            blockInt += messageBytes[i] * (BYTE_SIZE ** (i % blockSize))  # 对区块内的ASCII整数进行求和，一个字符对应一个ASCII整数
        blockInts.append(blockInt)
    return blockInts


def getTextFromBlocks(blockInts, messageLength, blockSize=DEFAULT_BLOCK_SIZE):
    # Converts a list of block integers to the original message string.
    # The original message length is needed to properly convert the last
    # block integer.
    message = []
    for blockInt in blockInts:
        blockMessage = []
        for i in range(blockSize - 1, -1, -1):
            if len(message) + i < messageLength:
                # Decode the message string for the 128 (or whatever
                # blockSize is set to) characters from this block integer.
                asciiNumber = blockInt // (BYTE_SIZE ** i)
                blockInt = blockInt % (BYTE_SIZE ** i)
                blockMessage.insert(0, chr(asciiNumber))
        message.extend(blockMessage)
    return ''.join(message)  # list to string


def encryptMessage(message, key, blockSize=DEFAULT_BLOCK_SIZE):
    # Converts the message string into a list of block integers, and then
    # encrypts each block integer. Pass the PUBLIC key to encrypt.
    encryptedBlocks = []
    n, e = key

    for block in getBlocksFromText(message, blockSize):
        # ciphertext = plaintext ^ e mod n
        encryptedBlocks.append(pow(block, e, n))
    return encryptedBlocks


def decryptMessage(encryptedBlocks, messageLength, key, blockSize=DEFAULT_BLOCK_SIZE):
    # Decrypts a list of encrypted block ints into the original message
    # string. The original message length is required to properly decrypt
    # the last block. Be sure to pass the PRIVATE key to decrypt.
    decryptedBlocks = []
    n, d = key
    for block in encryptedBlocks:
        # plaintext = ciphertext ^ d mod n
        decryptedBlocks.append(pow(block, d, n))
    return getTextFromBlocks(decryptedBlocks, messageLength, blockSize)


def readKeyFile(keyFilename):
    # Given the filename of a file that contains a public or private key,
    # return the key as a (n,e) or (n,d) tuple value.
    fo = open(keyFilename)
    content = fo.read()
    fo.close()
    keySize, n, EorD = content.split(',')
    return (int(keySize), int(n), int(EorD))


def encryptAndWriteToFile(messageFilename, keyFilename, message, blockSize=DEFAULT_BLOCK_SIZE):
    # Using a key from a key file, encrypt the message and save it to a
    # file. Returns the encrypted message string.
    keySize, n, e = readKeyFile(keyFilename)

    # Check that key size is greater than block size.
    if keySize < blockSize * 8: # * 8 to convert bytes to bits
        sys.exit('ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or greater than the key size. Either decrease the block size or use different keys.' % (blockSize * 8, keySize))


    # Encrypt the message
    encryptedBlocks = encryptMessage(message, (n, e), blockSize)

    # Convert the large int values to one string value.
    for i in range(len(encryptedBlocks)):
        encryptedBlocks[i] = str(encryptedBlocks[i])
    encryptedContent = ','.join(encryptedBlocks)

    # Write out the encrypted string to the output file.
    encryptedContent = '%s_%s_%s' % (len(message), blockSize, encryptedContent)
    fo = open(messageFilename, 'w')
    fo.write(encryptedContent)
    fo.close()
    # Also return the encrypted string.
    return encryptedContent


def readFromFileAndDecrypt(messageFilename, keyFilename):
    # Using a key from a key file, read an encrypted message from a file
    # and then decrypt it. Returns the decrypted message string.
    keySize, n, d = readKeyFile(keyFilename)


    # Read in the message length and the encrypted message from the file.
    fo = open(messageFilename)
    content = fo.read()
    messageLength, blockSize, encryptedMessage = content.split('_')
    messageLength = int(messageLength)
    blockSize = int(blockSize)

    # Check that key size is greater than block size.
    if keySize < blockSize * 8: # * 8 to convert bytes to bits
        sys.exit('ERROR: Block size is %s bits and key size is %s bits. The RSA cipher requires the block size to be equal to or greater than the key size. Did you specify the correct key file and encrypted file?' % (blockSize * 8, keySize))

    # Convert the encrypted message into large int values.
    encryptedBlocks = []
    for block in encryptedMessage.split(','):
        encryptedBlocks.append(int(block))

    # Decrypt the large int values.
    return decryptMessage(encryptedBlocks, messageLength, (n, d), blockSize)


# If rsaCipher.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    # python -m cProfile makeRsaKeys.py
    main()
