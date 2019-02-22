from ext import db

class UserModel(db.Model): # "user_model"
    _tablename_ = "something_else"

    
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True)
    password = db.Column(db.String, unqique = True)