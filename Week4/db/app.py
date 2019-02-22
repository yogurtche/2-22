from flask import Flask
from ext import db


app FLask(_name_)
app.config["SQLALCHEMY_DATABASE_URI"]='slqlite:///test1.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=True


db.init_app(app)


@app.before_first_request
def create():
    db.create_all()


@app.route
def route():
    return "Hello World!"


# app.register_blueprint(student, url_prefix = "/web")
# app.register_blueprint(restful, url_prefix = "/rest")
# app.register_blueprint(i_user, url_prefix = "/api/v2/user")