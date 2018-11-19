import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast
from Crypto.Cipher import PKCS1_OAEP

def enc_rsa(test):
    random_generator = Random.new().read
    key = RSA.generate(1024, random_generator)
    p=key.publickey()
    encryptor = PKCS1_OAEP.new(p)
    encrypted = encryptor.encrypt(test)
    return encrypted,key




def dec_rsa(test,key):
    decryptor = PKCS1_OAEP.new(key)
    decrypted = decryptor.decrypt(ast.literal_eval(str(test)))
    return decrypted.decode("ASCII")

