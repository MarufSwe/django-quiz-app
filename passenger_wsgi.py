import os
import sys

# Add the project directory to the sys.path
sys.path.insert(0, os.path.dirname(__file__) + '/django_quiz')

# Set the settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'config.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
