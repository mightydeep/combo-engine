import os, logging, codecs, mimetypes, hashlib

from google.appengine.ext import webapp
from google.appengine.api import memcache

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
LIB_PATH = os.path.join(PROJECT_ROOT, 'lib')

class ComboHandler(webapp.RequestHandler):
    def get(self):
        content_type, content = self.combine(self.request)
        self.response.headers.add_header('Content-Type', content_type)
        self.response.out.write(content)

    def get_file_content(self, file_name):
        file_path = os.path.join(LIB_PATH, file_name)
        try:
            file = codecs.open(file_path, 'r', 'utf-8')
            return file.read().lstrip(codecs.BOM_UTF8.decode('utf-8')).replace('\r\n', '\n').replace('\r', '\n')
        except:
            logging.warn('Could not read ' + file_path)
            return ''

    def combine(self, request):
        cache_key = hashlib.md5(request.url).hexdigest()
        
        data = memcache.get(cache_key)
        if data is not None:
            mime_type = data[0]
            content = data[1]
            
        else:
            file_list = request.arguments()
            mime_type = mimetypes.guess_type(file_list[0])[0]
            content = ''

            for file in file_list:
                content += self.get_file_content(file)

            memcache.add(cache_key, (mime_type, content))

        return mime_type, content
