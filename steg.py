from stegano import lsb
from stegano.lsbset import generators
import os
def enc(file_path,message,name):
    save_path='.\\enc_'+name+'.png' # cahnge this to change file save location
    #ext=fiel_path[-3:]
    #print(ext)
    secret = lsb.hide(file_path,message)
    secret.save(save_path)
    
    
def dec(file_path):
   m= lsb.reveal(file_path)
   return m





