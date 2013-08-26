'''
import sae
from teochew import wsgi

application = sae.create_wsgi_app(wsgi.app)
'''

import os
import django.core.handlers.wsgi
import sae

os.environ['DJANGO_SETTINGS_MODULE'] = 'teochew.settings'
application = sae.create_wsgi_app(django.core.handlers.wsgi.WSGIHandler())