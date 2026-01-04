"""
WSGI config for DanEmAnhTien project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from .db_connection import connect_db

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DanEmAnhTien.settings')

# Gọi hàm kết nối database tại đây
connect_db() 

application = get_wsgi_application()