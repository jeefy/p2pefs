"""
Gives network stats
"""

import tornado.web

class DefaultHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("default url")
        
    def post(self):
        self.write("default url post")