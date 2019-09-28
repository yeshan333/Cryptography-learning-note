#image转base64
import base64

filename = 'china.jpg'

with open(filename, "rb") as f:#转为二进制格式
    base64_data = base64.b64encode(f.read())#使用base64进行加密
    print(base64_data)
    file = open('img.txt','wt')  #写成文本格式
    file.write(base64_data.decode('utf-8'))  # bytes.decode(‘utf-8’)
    file.close()