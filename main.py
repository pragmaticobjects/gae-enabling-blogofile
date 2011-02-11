#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from google.appengine.ext import webapp
from google.appengine.ext.webapp import util
from google.appengine.ext.webapp import template

class IndexHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render('index.html', {}))

class PageHandler(webapp.RequestHandler):
    def get(self):
        #self.response.out.write(self.request.path)        
        self.response.out.write(template.render(self.request.path[1:] + '/index.html', {}))

class RssHandler(webapp.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'application/xml'
        self.response.out.write(template.render('blog/feed/index.xml', {}))

class RedirectedHandler(webapp.RequestHandler):
    def get(self):        
        #self.response.out.write(path)
        self.response.out.write(template.render(self.request.path[1:], {}))		

class MainHandler(webapp.RequestHandler):
    def get(self):
        path = self.request.path + '/index.html'
        #self.response.out.write(path)
        self.redirect(path)
        #self.response.out.write('Main')
        #self.response.out.write(self.request.path)
        #self.response.out.write(template.render('index.html', {}))

def main():
    application = webapp.WSGIApplication([
        ('/', IndexHandler),
        ('/blog/feed', RssHandler),
        ('/blog', PageHandler),        
        ('/blog/.*/[\w\.-]+(?<!\.html$)', MainHandler),
        ('/blog/[\w\.-]+(?<!\.html$)', MainHandler),        
        ('/blog/.*', RedirectedHandler),

        ('/community', PageHandler),
        ('/community/.*/[\w\.-]+(?<!\.html$)', MainHandler),
        ('/community/[\w\.-]+(?<!\.html$)', MainHandler),        
        ('/community/.*', RedirectedHandler),

        ('/demo', PageHandler),
        ('/demo/.*/[\w\.-]+(?<!\.html$)', MainHandler),
        ('/demo/[\w\.-]+(?<!\.html$)', MainHandler),        
        ('/demo/.*', RedirectedHandler),

        ('/documentation', PageHandler),
        ('/documentation/.*/[\w\.-]+(?<!\.html$)', MainHandler),
        ('/documentation/[\w\.-]+(?<!\.html$)', MainHandler),        
        ('/documentation/.*', RedirectedHandler),
        
        #('.*', RenderHandler),
        #('/blog/.*/', MainHandler),        
        #('.*', Error404),        
    ], debug=True)
    
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
