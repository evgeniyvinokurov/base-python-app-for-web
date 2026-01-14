from bottle import redirect, route, view, post, request, get, response, auth_basic
from bottle import static_file

@route('/')
@view('python')
def feedback(name='World'):
    param = {}
    return param   

