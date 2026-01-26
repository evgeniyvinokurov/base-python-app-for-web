from bottle import default_app, run

import router
from projects.index.codes.index import router

app = default_app()
