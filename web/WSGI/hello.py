# hello.py

def application(envrion, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    body = '<h1>Hello, %s!</h1>' % (envrion['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]