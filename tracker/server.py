import os, sys

lib_path = os.path.abspath('')
sys.path.append(lib_path)

import tornado.ioloop
import tornado.web

import settings

from handlers.default import DefaultHandler
from handlers.fileList import FileListHandler

application = tornado.web.Application([
    (r"/", DefaultHandler),
    (r"/fileList", DefaultHandler),
])

if __name__ == "__main__":
    application.listen(settings.port, settings.address)
    tornado.ioloop.IOLoop.instance().start()