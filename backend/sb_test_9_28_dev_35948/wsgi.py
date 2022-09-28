"""
WSGI config for sb_test_9_28_dev_35948 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sb_test_9_28_dev_35948.settings')

application = get_wsgi_application()
