#!/usr/bin/env python
#
# Copyright 2011 Kevin H Le
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
        self.response.out.write(template.render(self.request.path[1:] + '/index.html', {}))

class RssHandler(webapp.RequestHandler):
    def get(self):        
        self.response.headers['Content-Type'] = 'application/xml'
        self.response.out.write(template.render(self.request.path[1:] + '/index.xml', {}))

class RedirectedHandler(webapp.RequestHandler):
    def get(self):
        self.response.out.write(template.render(self.request.path[1:], {}))		

class PostHandler(webapp.RequestHandler):
    def get(self):        
        self.redirect(self.request.path + '/index.html')        

def main():
    application = webapp.WSGIApplication([
        ('/', IndexHandler),        
        ('/\w+/?$', PageHandler),        
        ('/blog[/?[\w\.-]*]*/feed$', RssHandler),                
        ('^[/\w\.-]+\.html$', RedirectedHandler),
        ('^[/\w\.-]+(?<!\.html)$', PostHandler),
        
        #('.*', Error404),        
                
    ], debug=True)
    
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()