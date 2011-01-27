import os, logging, re, codecs

#PROJECT_ROOT = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
LIB_PATH = os.path.join(PROJECT_ROOT, 'lib')

def get_file_content(file_name, **kwargs):
    file_path = os.path.join(LIB_PATH, file_name)
    try:
        file = codecs.open(file_path, 'r', 'utf-8')
        return file.read().lstrip(codecs.BOM_UTF8.decode('utf-8')).replace('\r\n', '\n').replace('\r', '\n')
    except:
        return ''

def combine(files, **kwargs):
    content = ''

    for file in files:
        content += get_file_content(file)

    return content
