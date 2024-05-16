from bottle import redirect, route, view, post, request, get, response, auth_basic
from bottle import static_file


from projects.xmla.codes.xmla import router
from projects.roaches.codes.race import router
from projects.feedback.codes.feedback import router


@route('/')
@view('index')
def catalog(name='World'):
    param = {}
    return param   