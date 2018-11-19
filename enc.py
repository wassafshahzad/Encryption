from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import os





class Enc:
    def __init__(self):
        return

    def pad(self,s):
        c=b'\0'*(AES.block_size-len(s)%AES.block_size)
        return s+c
    

    def encrypt(self,m,key):
        m=pad(m,AES.block_size)
        iv=(Random.new().read(AES.block_size))
        ciper = AES.new(key,AES.MODE_CBC,iv)
        return iv+ciper.encrypt(m)
        

    def decrypt(self,m,key):
        iv=m[:AES.block_size]
        ciper = AES.new(key,AES.MODE_CBC,iv)
        plain=ciper.decrypt(m[AES.block_size:])
        return  unpad(plain,AES.block_size)#plain.rstrip(b'\0') 
         



