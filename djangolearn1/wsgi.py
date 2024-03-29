"""
WSGI config for djangolearn1 project.

It exposes the WSGI callable as a module-level variable named ``application``.cd

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangolearn1.settings')

application = get_wsgi_application()
