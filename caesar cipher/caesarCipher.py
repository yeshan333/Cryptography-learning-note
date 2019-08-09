# Caesar Cipher
# http://inventwithpython.com/hacking (BSD Licensed)
# 凯撒加密法，此程序用于加密或解密字母

import pyperclip

# 待加密（encrypt）或解密（decrypt）字符串
message = 'This is my secret message.'

# 用于加密或解密的 密钥
key = 13

# 设置程序的加密解密模式：'encrypt' or 'decrypt'
mode = 'encrypt' # set to 'encrypt' or 'decrypt'

# 存放加密解密程序的符号集合，字符串常量
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# 用于存储加密或解密后的message
translated = ''

# 将message中的所有小写字母转换为大写形式
message = message.upper()

# 根据LETTERS遍历待加密或解密的message
for symbol in message:
    if symbol in LETTERS:
        # 获取待加密或解密字符在LETTERS中的位置
        num = LETTERS.find(symbol) # get the number of the symbol
        # 凯撒加密法主算法
        if mode == 'encrypt':
            num = num + key  # 经加密后的字符在LETTERS里的索引
        elif mode == 'decrypt':
            num = num - key  # 经解密后的字符在LETTERS里的索引

        # 处理索引越界情况
        if num >= len(LETTERS):
            num = num - len(LETTERS)
        elif num < 0:
            num = num + len(LETTERS)

        # 添加加密或解密后的字符到translated
        translated = translated + LETTERS[num]

    else:
        # just add the symbol without encrypting/decrypting
        translated = translated + symbol

# 输出经加密或解密后的字符串
print(translated)

# 将加密或解密后的字符串复制到系统剪切板
pyperclip.copy(translated)
