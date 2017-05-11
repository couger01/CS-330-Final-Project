from flask import Flask, render_template, redirect, url_for
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
app.config['SECURITY_CHANGEABLE'] = True
app.config['SECURITY_SEND_REGISTER_EMAIL'] = False
app.config['SECURITY_CONFIRMABLE'] = False
app.config['SECURITY_POST_LOGIN_VIEW'] = '/main-page'
app.config['SECURITY_POST_LOGOUT_VIEW'] = '/main-page'
app.config['SECURITY_POST_REGISTER_VIEW'] = '/main-page'
app.config['SECURITY_POST_CHANGE_VIEW'] = '/main-page'
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

@app.route("/view")
def view_page():
    char = {'name': "Adelaide the Knight", 'age': 28, 'race': 'Human',
            'owner': 'Ashleigh', 'social_class': 'Freeman'}
    p_dist = [26, 1, 5, 5, 6, 4, 5]
    char['pcp_dist'] = p_dist
    a = {'sage': 'defeat the dragon king', 'epic': 'slay dragons',
         'belief': 'dragons are evil', 'glory': 'success at killing dragons',
         'flaw': 'secretly loves dragons and was pressured into killing them'}
    char['arcs'] = a
    char['bio'] = """A young-ish knight who actually likes dragons but
                     got forced into fighting them by her family."""
    attr = {'STR': 4, 'AGI': 4, 'END': 4, 'HLT': 4, 'WIL': 3, 'WIT':4, 'INT':4,
            'PER': 4, 'TOU': 4, 'LUK': 3, 'ADR': 4, 'MOB': 6, 'CAR': 8,
            'CHA': 5, 'GRIT': 1}
    char['attributes'] = attr
    char['skills'] = [('Athletics', 6), ('Climbing', 6)]
    char['boons'] = ['Beautiful', 'Tall', 'Natural Born Killer III']
    char['banes'] = ['Arrow Magnet', 'Honor']
    char['school'] = ['Officer', 7]
    char['cp'] = 11
    char['mp'] = 0
    char['profs'] = [('2H Sword', 7)]
    char['talents'] =  ['Flourishing Drills', 'Good Form', 'Accuracy',
                        'Helm-Splitter', 'Infighter']
    char['weapons'] = [['Katana', '2H Sword', 'M', '7(+2c)', '7(+1p)', '7(1)',
                        'Draw 4, Hand-Off, Heavy Weapon', 1]]
    char['armors'] = [['Stechhelm', 10, 9, 8, 'Full Head, Neck', 8,
                      'Hard, Restricts Breathing 3'],
                     ['Anima Cuirass', 7 ,7, 7, 'Belly, Chest, Side', 3, 'Hard']
                    ]

    return render_template("char_view_page.html", user=core.current_user, character=char)

@app.route('/settings/<email>')
def settings_page(email):
    return render_template("user_settings.html", user=core.current_user)

@login_required
@app.route('/delete')
def delete_account():
    user_datastore.delete_user(core.current_user)
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)