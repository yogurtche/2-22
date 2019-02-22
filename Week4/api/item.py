from flask import Blueprint

i_user = Blueprint('api', __name__, template_folder='templates')


@api.route('/')
def show():
    return 'I am Blueprint'