#! /usr/bin/python3

##Imports##
import time
start_time = time.time()

from Crypto.Cipher import DES3
from Crypto import Random
from Crypto.Util import Counter
from lib.file import p2pfes
import argparse
import uuid
import os

parser = argparse.ArgumentParser()

##CLI Arg Setup##
parser.add_argument("-n", "--nodenum", dest="nodenum", default=5,                  help="Number of nodes to distribute each chunk to (default 5, minimum 3)")
parser.add_argument("-c", "--chunks",  dest="chunks",  default=3,                  help="Minimum number of file chunks (default 3, minimum 2)")
parser.add_argument("-k", "--key",     dest="key",     default="This is a key123", help="Secret key for the file")
parser.add_argument("-f", "--file",    dest="file",                                help="Path to file", required=True)
parser.add_argument("-u", "--uuid",    dest="uuid",                                help="UUID of p2pfes files")
parser.add_argument("-e", "--encrypt", dest="encrypt", default=False,              help="Encrypt and break apart file to p2pfes files")
parser.add_argument("-d", "--decrypt", dest="decrypt", default=False,              help="Decrypt and join p2pfes files into new file")
args = parser.parse_args()

p2pfes = p2pfes(args.key)

if args.encrypt:
    response = encrypt(args.file, args.key, args.chunks)
elif args.decrypt:
    response = decrypt(args.uuid, args.key, args.filename)
else:
    response = "Must set -e (--encrypt) or -d (--decrypt) option to execute"
    
print(response)