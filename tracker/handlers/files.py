"""
Lists all files on a peer based on a peer's UUID
"""
import tornado.web
import sys, os

from lib.db import _execute

class FilesHandler(tornado.web.RequestHandler):
    def get(self):
        #Get File Info
        self.write("fileList get")
        
    def post(self):
        #Add File
        self.write("fileList post")