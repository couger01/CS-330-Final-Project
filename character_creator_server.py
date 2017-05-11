from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required, utils, LoginForm, core
from flask_bootstrap import Bootstrap
import psycopg2
import os


app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'super-secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///couger01'
app.config['SECURITY_PASSWORD_HASH'] = 'sha512_crypt'
app.config['SECURITY_PASSWORD_SALT'] = 'QuhGFFHFDHhsjjfs'
app.config['SECURITY_REGISTERABLE'] = True
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False
app.config['SECURITY_CONFIRMABLE'] = False
app.config['SECURITY_POST_LOGIN_VIEW'] = '/main-page'
app.config['SECURITY_POST_LOGOUT_VIEW'] = '/main-page'
app.config['SECURITY_POST_REGISTER_VIEW'] = '/main-page'
Bootstrap(app)

db = SQLAlchemy(app)

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    salt = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref=db.backref('users', lazy='dynamic'))
    def __init__(self, email, password, active, roles):
        self.email = email
        self.password = password
        self.active = active
        self.roles = roles

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

@app.before_first_request
def create_user():
    db.create_all()
#     encpassword = utils.encrypt_password('password')
#     user_datastore.create_user(email='matt@nobien.net', password=encpassword, salt=app.config['SECURITY_PASSWORD_SALT'])
    db.session.commit()

@app.route('/main-page')
def home():
    return render_template('main_page.html',user=core.current_user)

@app.route("/search")
def results_page():
    res = [[3, "eric.coughlin2014@gmail.com", "Adelaide the Mercenary"],
           [1, "eric.coughlin2014@gmail.com", "Phillip the Bastard"],
           [5, "Ashleigh", "Anna the Knight"],
           [7, "Anonymous", "Mildred the Surgeon"]]
    return render_template("search_results.html", user=core.current_user, results=res)

if __name__ == '__main__':
    print(app.config['SECURITY_CONFIRMABLE'])
    app.run(debug=True)
