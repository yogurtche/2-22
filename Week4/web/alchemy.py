from flask import Flask
from web.publcik import student 
from api.item import i_user
from api.restful import restful
from flask_aqlalchemy import SQLALCHEMY
from ext import def 
(self, parameter_list):
    raise NotImplementedError

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