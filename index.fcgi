#!/usr/bin/scl enable rh-python35 -- /home2/enjoys07/institutoisar.com.br/.venv/bin/python

import os
import sys
from flup.server.fcgi import WSGIServer
from django.core.wsgi import get_wsgi_application

# Adicione o caminho ao seu projeto e ao ambiente virtual
sys.path.insert(0, "/home2/enjoys07/institutoisar.com.br/Site-Instituto-Socioambiental-Renovar/")
os.environ['DJANGO_SETTINGS_MODULE'] = "core.settings"

def application(environ, start_response):
    # Defina os parâmetros FastCGI necessários manualmente
    environ.setdefault('REQUEST_METHOD', 'GET')
    environ.setdefault('SERVER_NAME', 'localhost')
    environ.setdefault('SERVER_PORT', '80')
    environ.setdefault('SERVER_PROTOCOL', 'HTTP/1.1')

    # Crie o aplicativo WSGI Django
    application = get_wsgi_application()

    # Retorne a resposta usando o aplicativo WSGI
    return application(environ, start_response)

if __name__ == '__main__':
    WSGIServer(application).run()
