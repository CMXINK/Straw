import base64


class Base64:
    def __init__(self):
        super(Base64, self).__init__()

    def decode(self, value):
        #  base64解密数据, 返回一个字符串数据
        return base64.b64decode(value.encode('utf-8')).decode('utf-8')

    def encode(self, value):
        # base64加密数据, 返回一个字符串数据

        return base64.b64encode(value.encode('utf-8')).decode('utf-8')

