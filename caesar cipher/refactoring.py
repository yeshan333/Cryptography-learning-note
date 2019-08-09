# 优化凯撒加密解密程序结构

LETTERS = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

def caesarCipher(message, mode, key):
    translated = ''
    global LETTERS

    for symbol in message:
        if symbol in LETTERS:
            num = LETTERS.find(symbol)
            
            if mode == 'encrypt':
                num = num + key
            elif mode == 'decrypt':
                num = num - key
            
            if num >= len(LETTERS):
                num = num - len(LETTERS)
            elif num < 0:
                num = num + len(LETTERS)
            
            translated = translated + LETTERS[num]
        else:
            translated = translated + symbol

    return translated

if __name__ == '__main__':
    message = 'This is my secret message.'
    key = 13 
    mode = 'encrypt'

    new_message = caesarCipher(message, mode, key)

    print(f'{new_message}')