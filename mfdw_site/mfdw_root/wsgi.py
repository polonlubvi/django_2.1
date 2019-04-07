"""
WSGI config for mfdw_site project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import logging
import logging.config

logging.config.fileConfig("logging.conf")

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mfdw_site.settings')

application = get_wsgi_application()
logging.debug(application)


