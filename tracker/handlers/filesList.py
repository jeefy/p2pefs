"""
Lists all files on a peer based on a peer's UUID
"""
import tornado.web
import sys, os

from lib.db import _execute

class FileListHandler(tornado.web.RequestHandler):
    def get(self):
        #Get Files for a peer
        self.write("fileList get")
        
    def post(self):
        #Batch add files for a peer
        self.write("fileList post")