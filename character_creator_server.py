from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required, utils, LoginForm, core
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField
from wtforms.validators import
from wtforms import DataRequired, AnyOf
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

class BuildForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    age = IntegerField("Age", validators=[])
    race = StringField("Race", validators=[DataRequired()])
    pcp_total = SelectField('PCP total', validators=[DataRequired()],
                            choices=[(18, '18'), (22, '22'), (26, '26'),
                                     (30, '34'), (34, '34')])
    pcp_race = SelectField("Race PCP", validators=[DataRequired()],
                           choices=[(1, 'Tier 1'), (2, 'Tier 2'), (4, 'Tier 3'),
                                    (6, 'Tier 4'), (8, 'Tier 5')])
    pcp_attr = SelectField("Attributes PCP", validators=[DataRequired()],
                           choices=[(1, '26'), (2, '29'), (3, '32'), (4, '35'),
                                    (5, '38'), (6, '40'), (7, '42'), (8, '44'),
                                    (9, '46'), (10, '48')])
    pcp_skills = SelectField("Skills PCP", validators=[DataRequired()],
                             choices=[(k+1, str(k*3)) for k in range(10)]
    pcp_profs = SelectField("Skills PCP", validators=[DataRequired()],
                            choices=[(k+1, str(k*3)) for k in range(10)])
    pcp_social = SelectField("Social Class PCP", validators=[DataRequired()],
                             choices=[(1, 'Slave'), (2, 'Peasant'),
                                      (3, 'Poor Freeman'), (4, 'High Freeman'),
                                      (6, 'Minor Noble'), (7, 'Landed Noble'),
                                      (8, 'High Noble'), (9, 'Royalty'),
                                      (10, 'High Royalty')])
    pcp_boons_banes = SelectField("Boons and Banes PCP",
                                  validators=[DataRequired()],
                                  choices=[(k+1, str((k-3)*5)) for k in range(10)])
    arc_saga = StringField('Saga Arc', validators=[])
    arc_epic = StringField('Sage Arc', validators=[])
    arc_glory = StringField('Sage Arc', validators=[])
    arc_belief = StringField('Sage Arc', validators=[])
    arc_flaw = StringField('Sage Arc', validators=[])
    bio = TextAreaField("Character Bio", validators=[])



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
    characters = db.relationship("Characters")
    def __init__(self, email, password, active, roles):
        self.email = email
        self.password = password
        self.active = active
        self.roles = roles

class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'))
    name = db.Column(db.String(255))
    age = db.Column(db.Integer)
    race = db.Column(db.String(255))
    owner = db.Column(db.String(255))
    social_class = db.Column(db.String(255))
    sage = db.Column(db.String(255))
    epic = db.Column(db.String(255))
    belief = db.Column(db.String(255))
    glory = db.Column(db.String(255))
    flaw = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    STR = db.Column(db.Integer)
    AGI = db.Column(db.Integer)
    END = db.Column(db.Integer)
    HLT = db.Column(db.Integer)
    WIL = db.Column(db.Integer)
    WIT = db.Column(db.Integer)
    INT = db.Column(db.Integer)
    PER = db.Column(db.Integer)
    TOU = db.Column(db.Integer)
    LUK = db.Column(db.Integer)
    ADR = db.Column(db.Integer)
    MOB = db.Column(db.Integer)
    CAR = db.Column(db.Integer)
    CHA = db.Column(db.Integer)
    GRIT = db.Column(db.Integer)
    cp = db.Column(db.Integer)
    mp = db.Column(db.Integer)
    misc = db.relationship("Misc_char")
    weapon = db.relationship("Weapon_char")
    armour = db.relationship("Armour_char")
    boons = db.relationship("Boons")
    banes = db.relationship("Banes")
    skills = db.relationship("Skills")
    school = db.relationship("School")
    profs = db.relationship("Profs")

class Misc_char(db.Model):
    __tablename__ = 'misc_char'
    id = db.Column(db.Integer, primary_key=True)
    char = db.Column(db.Integer, db.ForeignKey('characters.id'))
    misc_id = db.Column(db.Integer, db.ForeignKey('misc_equipment.id'))

class Misc_equipment(db.Model):
    __tablename__ = 'misc_equipment'
    id = db.Column(db.Integer, primary_key=True)
    miscChar = db.relationship("Misc_char")

class Weapon_char(db.Model):
    __tablename__ = 'weapon_char'
    id = db.Column(db.Integer, primary_key=True)
    char = db.Column(db.Integer, db.ForeignKey('characters.id'))
    misc_id = db.Column(db.Integer, db.ForeignKey('weapons.id'))

class Weapons(db.Model):
    __tablename__ = 'weapons'
    id = db.Column(db.Integer, primary_key=True)
    miscChar = db.relationship("Weapon_char")

class Armour(db.Model):
    __tablename__ = 'armour'
    id = db.Column(db.Integer, primary_key=True)
    miscChar = db.relationship("Armour_char")

class Armour_char(db.Model):
    __tablename__ = 'armour_char'
    id = db.Column(db.Integer, primary_key=True)
    char = db.Column(db.Integer, db.ForeignKey('characters.id'))
    misc_id = db.Column(db.Integer, db.ForeignKey('armour.id'))

class Boons(db.Model):
    __tablename__ = 'boons'
    id = db.Column(db.Integer, primary_key=True)
    boon_1 = db.Column(db.String(255))
    boon_2 = db.Column(db.String(255))
    boon_3 = db.Column(db.String(255))
    boon_4 = db.Column(db.String(255))
    boon_5 = db.Column(db.String(255))
    boon_6 = db.Column(db.String(255))
    char = db.Column(db.Integer, db.ForeignKey('characters.id'))

class Banes(db.Model):
    __tablename__ = 'banes'
    id = db.Column(db.Integer, primary_key=True)
    bane_1 = db.Column(db.String(255))
    bane_2 = db.Column(db.String(255))
    bane_3 = db.Column(db.String(255))
    bane_4 = db.Column(db.String(255))
    bane_5 = db.Column(db.String(255))
    bane_6 = db.Column(db.String(255))
    char = db.Column(db.Integer, db.ForeignKey('characters.id'))

class Skills(db.Model):
    __tablename__ = 'skills'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    level = db.Column(db.Integer)
    char = db.Column(db.Integer, db.ForeignKey('characters.id'))

class School(db.Model):
    __tablename__ = 'school'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    level = db.Column(db.Integer)
    char = db.Column(db.Integer, db.ForeignKey('characters.id'))

class Profs(db.Model):
    __tablename__ = 'profs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    level = db.Column(db.Integer)
    char = db.Column(db.Integer, db.ForeignKey('characters.id'))



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
