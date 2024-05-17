from bottle import redirect, route, view, post, request, get, response, auth_basic
from bottle import static_file

import json

from . import users
from . import formvalidation


@route('/feedback/')
@view('feedback')
def feedback(name='World'):
    usersall = users.comments()
    param = {}
    param["usersall"] = usersall
    return param   


@post('/user/checkpost/')
def user_check():
    u = {}
    for key, value in request.forms.allitems():
        u[key] = value

    validated = formvalidation.validateform(u)
    if validated["status"]  == "ok":
        user = users.getuser(u["email"])
        if user is False:
            user = users.createuser(u)
            return '{"status": "ok", "key": "Success"}'
        else:
            return '{"status": "error", "key": "Only one feedback for email, please."}'
    else:
        return '{"status": "error", "key": "' + validated["key"] + '"}'
   

# ...

@route('/static/:path#.+#', name='static')
def static(path):
    return static_file(path, root='static')
