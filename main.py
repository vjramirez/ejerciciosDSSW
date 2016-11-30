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

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('<a href="/tarea1">Tarea 1</a><br/>'
							'<a href="/tarea2">Tarea 2</a><br/>'
		)
		
class Tarea1Handler(webapp2.RequestHandler):
	def get(self):
		self.response.write('Tarea 1')
		
class Tarea2Handler(webapp2.RequestHandler):
	def get(self):
		self.response.write('Tarea 2')

app = webapp2.WSGIApplication([
    ('/', MainHandler),
	('/tarea1', Tarea1Handler),
	('/tarea2', Tarea2Handler),
], debug=True)
