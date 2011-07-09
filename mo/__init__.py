from webob import Request

class HTTPMethodOverrideMiddleware(object):

    def __init__(self, application, *args, **kwargs):
        self.application = application

    def __call__(self, environ, start_response):
        override_method = ''

        if 'form-urlencoded' in environ['CONTENT_TYPE']:
            req = Request(environ)
            override_method = req.str_POST.get('_method', '').upper()

        if not override_method:
            override_method = environ.get('HTTP_X_HTTP_OVERRIDE_METHOD', '').upper()

        if override_method in ('PUT', 'DELETE', 'OPTIONS', 'PATCH'):
            environ['http_method_override.original_method'] = environ['REQUEST_METHOD']
            environ['REQUEST_METHOD'] = override_method

        return self.application(environ, start_response)

def make_method_override_middleware(app, global_conf, **kw):
    return HTTPMethodOverrideMiddleware(app, global_conf=global_conf, **kw)
