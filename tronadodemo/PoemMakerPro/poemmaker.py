# -*- encoding: utf-8 -*-
import os.path

import textwrap

import tornado.web
from tornado import  web
from tornado import  httpserver
from  tornado import  ioloop
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)



class hello(web.RequestHandler):
    def get(self, *args, **kwargs):
        self.write('hello worfld!')

class IndexHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        # self.write('登陆界面！')
        self.render('index.html')


class test(tornado.web.RequestHandler):
    def post(self):
        # self.write('登陆界面！')
        self.render('btzero_7_Director/index.html')


class simple(tornado.web.RequestHandler):
    def post(self):
        # self.write('登陆界面！')
        self.render('btzero_7_Director/simple.html')
class PoemPageHandler(tornado.web.RequestHandler):
    def post(self):
        noun1 = self.get_argument('noun1')
        noun2 = self.get_argument('noun2')
        verb = self.get_argument('verb')
        noun3 = self.get_argument('noun3')
        self.render('poem.html', roads=noun1, wood=noun2, made=verb,
                difference=noun3)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r"/index", IndexHandler),
                  (r"/poem", PoemPageHandler),
                  (r"/he",hello),
                  (r"/test",test),
                  (r"/simple",simple)],
        # template_path=os.path.join(os.path.dirname(__file__), "templates")
        static_path=os.path.join(os.path.dirname(__file__), "btzero_7_Director")
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()