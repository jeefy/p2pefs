"""
Lists all peers based on a file uuid
"""
import tornado.web
import sys, os

from lib.db import _execute

class PeersHandler(tornado.web.RequestHandler):
    def get(self):
        #Info on Peer
        self.write("peers get")
        
    def post(self):
        #Connect Peer
        self.write("peers post")