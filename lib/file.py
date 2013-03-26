#! /usr/bin/python3
from Crypto.Cipher import DES3
from Crypto import Random
from Crypto.Util import Counter
import uuid
import os

class p2pfes():
    def __init__(self, key, iv="12345678"):
        ##Set Up Encryption Object##
        self.cipher = DES3.new(key, DES3.MODE_CFB, iv)
        
    def encrypt(self, path, key, chunks):
        ##Generate file UUID##
        fileuuid   = str(uuid.uuid4())
        
        ##Check for valid file##
        if os.path.isfile(path) is False:
            print('Error -- File not valid')
            exit
        
        ##Math out chunkSize##
        chunksize  = round((os.path.getsize(path) / chunks) + 1)
        print('Chunksize: ' + str(chunksize))
        
        ## Open source, split, encrypt, write##
        files = []
        with open(path, mode="rb") as infile:
            for i in range(chunks):
                newfile = fileuuid + '_' + str(i+1)
                with open('files/' + newfile, mode="wb") as outfile:
                    chunk = infile.read(chunksize)
                    #if len(chunk) % 16 != 0:
                    #    chunk += ' ' * (16 - len(chunk) % 16)
                    outfile.write(self.cipher.encrypt(chunk))
                    files.append(newfile)
        return fileuuid
        
    
    def decrypt(self, uuid, key, new_filename):
        files = []
        for filename in os.listdir('files/'):
            if uuid in filename:
                files.append(filename)
        
        files.sort()
        with open('files/' + new_filename, mode="wb") as newfile:
            for path in files:
                with open(path, mode="rb") as oldfile:
                    newfile.write(self.cipher.decrypt(oldfile.read()))
        
        return new_filename