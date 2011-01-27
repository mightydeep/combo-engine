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
import logging

import combo

MIME_TYPES = {
    'js' : 'application/javascript',
    'css' : 'text/css'
}

class MainHandler(webapp.RequestHandler):
    def get(self):
        file_list = self.request.arguments()
        split_file = file_list[0].split('.')
        mime_type = MIME_TYPES[str(split_file[len(split_file) - 1])]
        self.response.headers.add_header('Content-Type', mime_type)
        self.response.out.write(combo.combine(self.request.arguments()))


def main():
    application = webapp.WSGIApplication([('/', MainHandler)],
                                         debug=True)
    util.run_wsgi_app(application)


if __name__ == '__main__':
    main()
