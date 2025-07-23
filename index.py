from bottle import default_app, run

import router
from projects.index.codes.index import router

application = default_app()
application.run()
