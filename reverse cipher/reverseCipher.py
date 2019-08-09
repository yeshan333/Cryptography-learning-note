# 反转加密

message = input("Please enter the message you want to encrypt：")

translate = ''

message_len = len(message) - 1

while message_len >= 0:
    translate += message[message_len]
    message_len -= 1

print(f'after encrypte：{translate}')