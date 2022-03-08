import base64

from Cryptodome.Cipher import AES
from binascii import b2a_hex, a2b_hex

# 如果text不足16位的倍数就用空格补足为16位
class AesCrypt():
    def __init__(self):
        self.key = 'cloudwisdomadjsn'.encode('utf-8')
        self.iv = b'5721678222017913'
    def add_to_16(self,text):
        if len(text.encode('utf-8')) % 16:
            add = 16 - (len(text.encode('utf-8')) % 16)
        else:
            add = 0
        text = text + ('\0' * add)
        return text.encode('utf-8')


    # 加密函数
    def encrypt(self,text):
        #key = 'cloudwisdomadjsn'.encode('utf-8')
        mode = AES.MODE_CBC
        #iv = b'5721678222017913'
        text = self.add_to_16(text)
        cryptos = AES.new(self.key, mode, self.iv)
        cipher_text1 = cryptos.encrypt(text)
        cipher_text = base64.b64encode(cipher_text1)
        # 因为AES加密后的字符串不一定是ascii字符集的，输出保存可能存在问题，所以这里转为16进制字符串
        #return b2a_hex(cipher_text)
        return cipher_text


    # 解密后，去掉补足的空格用strip() 去掉
    def decrypt(self,text):
        #key = 'cloudwisdomadjsn'.encode('utf-8')
        #iv = b'5721678222017913'
        mode = AES.MODE_CBC
        cryptos = AES.new(self.key, mode, self.iv)
        text1 = base64.b64decode(text)
        #plain_text = cryptos.decrypt(a2b_hex(text1))
        plain_text = cryptos.decrypt(text1)
        return bytes.decode(plain_text).rstrip('\0')



if __name__ == '__main__':
    #e = AesCrypt().encrypt("{'RQModel_CheckInfo': [{'Identity': '18611625312', 'DptDate': '2020-03-04', 'SearchMainAcct': 'False', 'SearchFlg': '3', 'ArrDate': '2020-02-26', 'Status': '1', 'SearchLockFlag': 'False'}], 'isformal': 'True', 'htlcd': 'lc01', 'staffpassword': 'sunwood', 'grpcd': 'lc', 'staffcd': '9897', 'mac': '6C-0B-84-08-06-78', 'token': '90B2815FB9AECFAB653162C388CC342F59DE6F1B'}")  # 加密
    b = "gHlNqppn3Hd7B3UfUVwaif7iM/qlRUk8ddSZ8r8//g74ZRYZW8jJC7gE8oeuNfO0lfZAE+7qnitVoXRB8Q6PL+u4b4Cqlj0dK+WEZobAIu80WAIIwAK65E+oMvwwgvIgOcIwiQdYCiAu3d8CWC8td0LAz3+/93U/Ja62bfZdG6oPA3TTwSmagPIzL0ni7mn9pH8CD1uZOrFiKmoJIY8Y6vKEPvN9D08+8jnjUcMz4PpXqXbzsxKBf9rRnXsuRIQabJri7CvibM5C/eGbUjqhFshL9rJxwRXGLXY2iVySOM2sFAuclbYj/ug/GS0Nx4yIAFZP4ar4EZmQ9mH+5OvJng=="
    #d = AesCrypt().decrypt(b)  # 解密
    #print("加密:", e)
    #print("解密:", d)