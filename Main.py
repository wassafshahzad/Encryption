from base64 import b64encode,b64decode
from os import urandom
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import os
from enc import Enc
from stegano import lsb
from rsa import *
from steg import *
from Crypto.PublicKey import RSA
import secrets

#image_path="C:\\Users\\\Desktop\\input.png" Example Image path 
#file_path='C:\\Users\\Desktop\\Enc.txt' Example file path
#name='haha' Example name

def enc_main(file_path,image_path,name):
    try:
        #path=os.getcwd()+file_path
        file=open(file_path,'r')
    
############AES encryption
        e=Enc()
        M=file.read()
        file.close()
        M=M.encode('ASCII')
        key =b64encode(os.urandom(16))

        m=e.encrypt(M,key)
        m=b64encode(m).decode("ASCII")
    

##### RSA Encryption

        k_m,p_key = enc_rsa(key)
        f=open('public_key_'+name+'.pem','wb') ## Change this to change rsa public key save location
        f.write(p_key.exportKey('PEM'))
        f.close()
        k_m=b64encode(k_m).decode("ASCII")

        m = m+'.'+k_m
        print('File encrypted ')
        
##Stagano######################
        #path_image=os.getcwd()+image_path
        #path_save=os.getcwd()+save_path
        enc(image_path,m,name)
    except:
        print('File Not found')


def dec_main(file_path,rsa_file,name):
#######################Decr##########################   
    e=Enc()
    try:
        f=open(rsa_file,'rb')
        p_key=RSA.importKey(f.read())
        f.close()
        M=dec(file_path)
        m=M.split('.')[0]
        m=b64decode(m.encode("ASCII"))
        k_m=M.split('.')[1]
        k_m=b64decode(k_m.encode("ASCII"))
        key1=dec_rsa(k_m,p_key)
        key1= key1.encode("ASCII")
        M=e.decrypt(m,key1)
        f=open('decrypted_file_'+name+'.txt','w')
        f.write(M.decode('ASCII'))
        f.close()
    except:
        print('file not found')
        return
    
############################################Main code#########################33
while(True):
    choice=input("Enter 1-for Encyption 2-for decryption 3-to Exit\n")
    if (choice==str(1)):
        file_path=input('Enter file path of the file to encrypt\n')
        name=input('Enter name to save encrypted image as\n')
        image_path=input('Enter path of image for stegnography\n')
        enc_main(file_path,image_path,name)
    if (choice==str(2)):
        file_path=input('Enter file path of the file to decrypt\n')
        name=input('Enter name to save decrypted file as\n')
        rsa_path=input('Enter path of rsa public key file for this encrypted file\n')
        dec_main(file_path,rsa_path,name)
    if (choice ==str(3)):
        print('\nexit\n')
        break
