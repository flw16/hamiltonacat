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
import webapp2
import os
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
	loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
	extensions=['jinja2.ext.autoescape'],
	autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/home.html')
        self.response.write(template.render({'title': 'Home'}))

class SecondHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/about.html')
        self.response.write(template.render({'title': 'About Me'}))

class ThirdHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/gallery.html')
        self.response.write(template.render({'title': 'Image Gallery'}))

class FourthHandler(webapp2.RequestHandler):
    def get(self):
    	template = JINJA_ENVIRONMENT.get_template('templates/map.html')
        self.response.write(template.render({'title': 'HSHV'}))



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/home.html', MainHandler),
    ('/about.html', SecondHandler),
    ('/gallery.html', ThirdHandler),
    ('/map.html', FourthHandler)],
	debug=True)