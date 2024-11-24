from . import auth, model

def init(app, database):
    auth.init(app, database)
    model.init(app)