from bottle import redirect, route, view, post, request, get, response, auth_basic
from bottle import static_file

@route('/python/')
@view('python')
def feedback(name='World'):
    param = {}
    return param   

@route('/')
@view('index')
def feedback(name='World'):
    param = {}
    return param   

@route('/more')
@view('more')
def feedback(name='World'):
    param = {}
    return param   

@route('/faq/')
@view('faq')
def feedback(name='World'):
    param = {}
    return param   

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')
