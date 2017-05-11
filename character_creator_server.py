from flask import Flask, render_template, redirect, url_for, request, Response
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
import requests as req
import json


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
app.config['SECURITY_POST_LOGIN_VIEW'] = '/'
app.config['SECURITY_POST_LOGOUT_VIEW'] = '/'
app.config['SECURITY_POST_REGISTER_VIEW'] = '/'
app.config['SECURITY_POST_CHANGE_VIEW'] = '/'
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
    total_pcp = db.Column(db.Integer)
    race_pcp = db.Column(db.Integer)
    attributes_pcp = db.Column(db.Integer)
    skills_pcp = db.Column(db.Integer)
    proficiences_pcp = db.Column(db.Integer)
    social_pcp = db.Column(db.Integer)
    boons_banes_pcp = db.Column(db.Integer)
    sage = db.Column(db.String(255))
    epic = db.Column(db.String(255))
    belief = db.Column(db.String(255))
    glory = db.Column(db.String(255))
    flaw = db.Column(db.String(255))
    bio = db.Column(db.String(512))
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
    name = db.Column(db.String(255))
    unit = db.Column(db.String(255))
    cost = db.Column(db.Integer)
    miscChar = db.relationship("Misc_char")

    def row2dict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = str(getattr(self, column.name))

        return d

class Weapon_char(db.Model):
    __tablename__ = 'weapon_char'
    id = db.Column(db.Integer, primary_key=True)
    char = db.Column(db.Integer, db.ForeignKey('characters.id'))
    weap_id = db.Column(db.Integer, db.ForeignKey('weapons.id'))

class Weapons(db.Model):
    __tablename__ = 'weapons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    weapon_type = db.Column(db.String(255))
    reach = db.Column(db.String(255))
    swing = db.Column(db.String(255))
    thrust = db.Column(db.String(255))
    defense_guard = db.Column(db.String(255))
    special = db.Column(db.String(255))
    weight = db.Column(db.String(255))
    cost = db.Column(db.String(255))
    weapChar = db.relationship("Weapon_char")

    def row2dict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = str(getattr(self, column.name))

        return d

class Armour(db.Model):
    __tablename__ = 'armour'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    AVC = db.Column(db.Integer)
    AVP = db.Column(db.Integer)
    AVB = db.Column(db.Integer)
    coverage = db.Column(db.String(255))
    special = db.Column(db.String(255))
    weight = db.Column(db.Float)
    cost = db.Column(db.String(255))
    armourChar = db.relationship("Armour_char")

    def row2dict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = str(getattr(self, column.name))

        return d

class Armour_char(db.Model):
    __tablename__ = 'armour_char'
    id = db.Column(db.Integer, primary_key=True)
    char = db.Column(db.Integer, db.ForeignKey('characters.id'))
    armor_id = db.Column(db.Integer, db.ForeignKey('armour.id'))

class Boons(db.Model):
    __tablename__ = 'boons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    cost = db.Column(db.String(255))
    char = db.Column(db.Integer, db.ForeignKey('characters.id'))

    def row2dict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = str(getattr(self, column.name))

        return d



class Banes(db.Model):
    __tablename__ = 'banes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    cost = db.Column(db.String(255))
    char = db.Column(db.Integer, db.ForeignKey('characters.id'))

    def row2dict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = str(getattr(self, column.name))

        return d

class Skills(db.Model):
    __tablename__ = 'skills'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    level = db.Column(db.Integer)
    char = db.Column(db.Integer, db.ForeignKey('characters.id'))

    def row2dict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = str(getattr(self, column.name))

        return d

class School(db.Model):
    __tablename__ = 'school'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    level = db.Column(db.Integer)
    char = db.Column(db.Integer, db.ForeignKey('characters.id'))

    def row2dict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = str(getattr(self, column.name))

        return d

class Profs(db.Model):
    __tablename__ = 'profs'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    level = db.Column(db.Integer)
    char = db.Column(db.Integer, db.ForeignKey('characters.id'))

    def row2dict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = str(getattr(self, column.name))

        return d

class Talents(db.Model):
    __tablename__ = 'talents'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    char = db.Column(db.Integer, db.ForeignKey('characters.id'))

    def row2dict(self):
        d = {}
        for column in self.__table__.columns:
            d[column.name] = str(getattr(self, column.name))

        return d



user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

@app.before_first_request
def create_user():
    db.create_all()
#     encpassword = utils.encrypt_password('password')
#     user_datastore.create_user(email='matt@nobien.net', password=encpassword, salt=app.config['SECURITY_PASSWORD_SALT'])
    new_character= Characters(user=1,name="Adelaide the Knight",age=28,race='Human',owner="Ashleigh",social_class='Freeman',total_pcp=26,race_pcp=1,attributes_pcp=5,skills_pcp=5,proficiences_pcp=6,social_pcp=4,boons_banes_pcp=5,sage='defeat the dragon king',epic='slay dragons'\
    ,belief='dragons are evil',flaw='secretly loves dragons and was pressured into killing them',bio="""A young-ish knight who actually likes dragons
    but got forced into fighting them by her family.""",STR=4,AGI=4,END=4,HLT=4,WIL=3,WIT=4,INT=4,PER=4,TOU=4,LUK=3,ADR=4,MOB=6,CAR=8,CHA=5,GRIT=1,\
    cp=11,mp=0)
    new_character_skill= Skills(name='Athletics',level=6,char=1)
    new_character_skill2=Skills(name='Climbing',level=6,char=1)
    new_character_boons=Boons(name='Beautiful',char=1)
    new_character_boons2=Boons(name='Tall',char=1)
    new_character_boons3=Boons(name='Natural Born Killer III',char=1)
    new_character_banes=Banes(name='Arrow Magnet',char=1)
    new_character_banes2=Banes(name='Honor',char=1)
    new_character_school=School(name='Officer',level=7, char=1)
    new_character_profs = Profs(name='2H Swords',level=7,char=1)
    new_character_talent = Talents(name='Flourishing Drills',char=1)
    new_character_talent2 = Talents(name='Good Form',char=1)
    new_character_talent3 = Talents(name='Accuracy',char=1)
    new_character_talent4 = Talents(name='Helm-Splitter',char=1)
    new_character_talent5 = Talents(name='Infighter',char=1)
    new_weapon = Weapons(name='Katana',weapon_type='2H Sword',reach='M',\
    swing='7(+2c)',thrust='7(+1p)',defense_guard='7(1)',\
    special='Draw 4, Hand-Off, Heavy Weapon',weight=1)
    new_weapon_conn = Weapon_char(char=1,weap_id=1)
    new_armor = Armour(name='Stechhelm',AVC=10,AVP=9,AVB=8,coverage='Full Head, Neck',weight=8,special='Hard, Restricts Breathing 3')
    new_armor2 = Armour(name='Anima Cuirass',AVC=7,AVP=7,AVB=7,coverage='Belly, Chest, Side',weight=3,special='Hard')
    new_armor_conn = Armour_char(char=1,armor_id=1)
    new_armor_conn2 = Armour_char(char=1,armor_id=2)
    with open('raw_text_sources/data.json') as datafile:
        data = json.loads(datafile.read(), encoding='utf-8')
    print(data['armor'])
    # for boon in data['boons']:
    #     db.session.add(Boons(name=boon[0],cost=boon[1]))
    # for bane in data['banes']:
    #     db.session.add(Banes(name=bane[0],cost=bane[1]))
    # for skill in data['skills']:
    #     db.session.add(Skills(name=skill))
    # for weapon in data['weapons']:
    #     db.session.add(Weapons(name=weapon[0],weapon_type=weapon[1],reach=weapon[2],swing=weapon[3],thrust=weapon[4],defense_guard=weapon[5],special=weapon[6],weight=weapon[7],cost=weapon[8]))
    # for armor in data['armor']:
    #    db.session.add(Armour(name=armor[0],AVC=int(armor[1]),AVP=int(armor[2]),AVB=int(armor[3]),coverage=armor[4],weight=armor[6],special=armor[5],cost=armor[7]))

    # db.session.add(new_character)
    # db.session.add(new_character_skill)
    # db.session.add(new_character_skill2)
    # db.session.add(new_character_boons)
    # db.session.add(new_character_boons2)
    # db.session.add(new_character_boons3)
    # db.session.add(new_character_banes)
    # db.session.add(new_character_banes2)
    # db.session.add(new_character_school)
    # db.session.add(new_character_profs)
    # db.session.add(new_character_talent)
    # db.session.add(new_character_talent2)
    # db.session.add(new_character_talent3)
    # db.session.add(new_character_talent4)
    # db.session.add(new_character_talent5)
    # db.session.add(new_weapon)
    # db.session.add(new_weapon_conn)
    # db.session.add(new_armor)
    # db.session.add(new_armor2)
    # db.session.add(new_armor_conn)
    # db.session.add(new_armor_conn2)
    db.session.commit()

@app.route('/')
def home():
    return render_template('main_page.html',user=core.current_user)

@app.route("/search")
def results_page():
    res = [[3, "eric.coughlin2014@gmail.com", "Adelaide the Mercenary"],
           [1, "eric.coughlin2014@gmail.com", "Phillip the Bastard"],
           [5, "Ashleigh", "Anna the Knight"],
           [7, "Anonymous", "Mildred the Surgeon"]]
    return render_template("search_results.html", user=core.current_user, results=res)

@app.route("/view/<id>")
def view_page(id):
    fc=db.session.query(Characters).filter(Characters.id == id).first()
    fc_skills = db.session.query(Skills).filter(Skills.char == fc.id).all()
    fc_boons = db.session.query(Boons).filter(Boons.char == fc.id).all()
    fc_banes = db.session.query(Banes).filter(Banes.char == fc.id).all()
    fc_schools = db.session.query(School).filter(School.char == fc.id).all()
    fc_profs = db.session.query(Profs).filter(Profs.char == fc.id).all()
    fc_talents = db.session.query(Talents).filter(Talents.char == fc.id).all()
    fc_weapons = db.session.query(Weapons).filter(fc.id == Weapon_char.char).filter(Weapon_char.weap_id == Weapons.id).all()
    fc_armors = db.session.query(Armour).filter(fc.id == Armour_char.char).filter(Armour_char.armor_id == Armour.id).all()
    char = {'name': fc.name, 'age': fc.age, 'race': fc.race,
            'owner': fc.owner, 'social_class': fc.social_class}
    p_dist = [fc.total_pcp, fc.race_pcp, fc.attributes_pcp, fc.skills_pcp, fc.proficiences_pcp, fc.social_pcp, fc.boons_banes_pcp]
    char['pcp_dist'] = p_dist
    a = {'sage': fc.sage, 'epic': fc.epic,
         'belief': fc.belief, 'glory': fc.glory,
         'flaw': fc.flaw}
    char['arcs'] = a
    char['bio'] = fc.bio
    attr = {'STR': fc.STR, 'AGI': fc.AGI, 'END': fc.END, 'HLT': fc.HLT, 'WIL': fc.WIL, 'WIT':fc.WIT, 'INT':fc.INT,
            'PER': fc.PER, 'TOU': fc.TOU, 'LUK': fc.LUK, 'ADR': fc.ADR, 'MOB': fc.MOB, 'CAR': fc.CAR,
            'CHA': fc.CHA, 'GRIT': fc.GRIT}
    char['attributes'] = attr
    skills_list = []
    for skill in fc_skills:
        st = (skill.name, skill.level)
        skills_list.append(st)
    char['skills'] = skills_list
    boons_list = []
    for boon in fc_boons:
        boons_list.append(boon.name)
    char['boons'] = boons_list
    banes_list = []
    for bane in fc_banes:
        banes_list.append(bane.name)
    char['banes'] = banes_list
    schools_list = []
    for school in fc_schools:
        schools_list.append(school.name)
        schools_list.append(school.level)
    char['school'] = schools_list
    char['cp'] = fc.cp
    char['mp'] = fc.mp
    profs_list = []
    for prof in fc_profs:
        pt = (prof.name,prof.level)
        profs_list.append(pt)
    char['profs'] = profs_list
    talents_list = []
    for talent in fc_talents:
        talents_list.append(talent.name)
    char['talents'] =  talents_list
    weapons_list = []
    for weapon in fc_weapons:
        weapon_list = []
        weapon_list.append(weapon.name)
        weapon_list.append(weapon.weapon_type)
        weapon_list.append(weapon.reach)
        weapon_list.append(weapon.swing)
        weapon_list.append(weapon.thrust)
        weapon_list.append(weapon.defense_guard)
        weapon_list.append(weapon.special)
        weapon_list.append(weapon.weight)
        weapons_list.append(weapon_list)
    char['weapons'] = weapons_list
    armors_list = []
    for armor in fc_armors:
        armor_list = []
        armor_list.append(armor.name)
        armor_list.append(armor.AVC)
        armor_list.append(armor.AVP)
        armor_list.append(armor.AVB)
        armor_list.append(armor.coverage)
        armor_list.append(armor.weight)
        armor_list.append(armor.special)
        armors_list.append(armor_list)

    char['armors'] = armors_list

    return render_template("char_view_page.html", user=core.current_user, character=char)

@app.route('/api/weapons/search/<name>', methods=['GET'])
def get_weapon(name):
    weapons_list = []
    weapons = db.session.query(Weapons).filter(Weapons.name.like(name.title() + '%')).all()
    return json.dumps([weapon.row2dict() for weapon in weapons])

@app.route('/api/weapons', methods=['GET'])
def get_all_weapons():
    weapons = db.session.query(Weapons).all()
    return json.dumps([weapon.row2dict() for weapon in weapons])

@app.route('/api/armors/search/<name>',methods=['GET'])
def get_armor(name):
    armors = db.session.query(Armour).filter(Armour.name.like(name.title()+'%')).all()
    return json.dumps([armor.row2dict() for armor in armors])

@app.route('/api/armors',methods=['GET'])
def get_all_armors():
    armors = db.session.query(Armour).all()
    return json.dumps([armor.row2dict() for armor in armors])

@app.route('/api/equipment/search/<name>', methods=['GET'])
def get_equipment(name):
    equipment = db.session.query(Misc_equipment).filter(Misc_equipment.name.like(name.title()+'%')).all()
    return json.dumps([piece.row2dict() for piece in equipment])

@app.route('/api/equipment', methods=['GET'])
def get_all_equipment():
    equipment = db.session.query(Misc_equipment).all()
    return json.dumps([piece.row2dict() for piece in equipment])

@app.route('/api/boons/search/<name>', methods=['GET'])
def get_boons(name):
    boons = db.session.query(Boons).filter(Boons.name.like(name.title()+'%')).all()
    return json.dumps([boon.row2dict() for boon in boons])

@app.route('/api/boons', methods=['GET'])
def get_all_boons():
    boons = db.session.query(Boons).all()
    return json.dumps([boon.row2dict() for boon in boons])

@app.route('/api/banes/search/<name>', methods=['GET'])
def get_banes(name):
    banes = db.session.query(Banes).filter(Banes.name.like(name.title()+'%')).all()
    return json.dumps([bane.row2dict() for bane in banes])

@app.route('/api/banes', methods=['GET'])
def get_all_banes():
    banes = db.session.query(Banes).all()
    return json.dumps([bane.row2dict() for bane in banes])

@app.route('/api/skills/search/<name>', methods=['GET'])
def get_skills(name):
    skills = db.session.query(Skills).filter(Skills.name.like(name.title()+'%')).all()
    return json.dumps([skill.row2dict() for skill in skills])

@app.route('/api/skills', methods=['GET'])
def get_all_skills():
    skills = db.session.query(Skills).all()
    return json.dumps([skill.row2dict() for skill in skills])

@app.route('/api/school/search/<name>', methods=['GET'])
def get_school(name):
    schools = db.session.query(School).filter(School.name.like(name.title()+'%')).all()
    return json.dumps([school.row2dict() for school in schools])

@app.route('/api/school', methods=['GET'])
def get_all_schools():
    schools = db.session.query(School).all()
    return json.dumps([school.row2dict() for school in schools])

@app.route('/api/profs/search/<name>', methods=['GET'])
def get_profs(name):
    profs = db.session.query(Profs).filter(Profs.name.like(name.title()+'%')).all()
    return json.dumps([prof.row2dict() for prof in profs])

@app.route('/api/profs', methods=['GET'])
def get_all_profs():
    profs = db.session.query(Profs).all()
    return json.dumps([prof.row2dict() for prof in profs])

@app.route('/api/talents/search/<name>', methods=['GET'])
def get_talents(name):
    talents = db.session.query(Talents).filter(Talents.name.like(name.title()+'%')).all()
    return json.dumps([talent.row2dict() for talent in talents])

@app.route('/api/talents', methods=['GET'])
def get_all_talents():
    talents = db.session.query(Talents).all()
    return json.dumps([talent.row2dict() for talent in talents])

@app.route('/save',methods=['POST'])
def insert():
    character = Character(
    name=request.form.get('name'),
    age=request.form.get('age'),
    race=request.form.get('race'),
    pcp_total=request.form.get('pcp_total'),
    pcp_race=request.form.get('pcp_race'),
    pcp_attr=request.form.get('pcp_attr'),
    pcp_skills=request.form.get('pcp_skills'),
    pcp_profs=request.form.get('pcp_profs'),
    pcp_social=request.form.get('pcp_social'),
    pcp_boons_banes=request.form.get('pcp_boons_banes'),
    sage=request.form.get('arc_saga'),
    epic=request.form.get('arc_epic'),
    belief=request.form.get('arc_belief'),
    glory=request.form.get('arc_glory'),
    flaw=request.form.get('arc_flaw'),
    bio=request.form.get('bio'),
    STR=request.form.get('attr_str'),
    AGI=request.form.get('attr_agi'),
    END=request.form.get('attr_end'),
    HLT=request.form.get('attr_hlt'),
    WIL=request.form.get('attr_wil'),
    WIT=request.form.get('attr_wit'),
    INT=request.form.get('attr_int'),
    PER=request.form.get('attr_per'),
    TOU=request.form.get('attr_tou'),
    LUK=request.form.get('attr_luk')
    )
    skill_1 = Skill(
    name=request.form.get('skill_1_name'),
    level=request.form.get('skill_1_level'),
    char = character.id
    )
    skill_2 = Skill(
    name=request.form.get('skill_2_name'),
    level=request.form.get('skill_2_level'),
    char = character.id
    )
    skill_3 = Skill(
    name=request.form.get('skill_3_name'),
    level=request.form.get('skill_3_level'),
    char = character.id
    )
    skill_4 = Skill(
    name=request.form.get('skill_4_name'),
    level=request.form.get('skill_4_level'),
    char = character.id
    )
    skill_5 = Skill(
    name=request.form.get('skill_5_name'),
    level=request.form.get('skill_5_level'),
    char = character.id
    )
    skill_6 = Skill(
    name=request.form.get('skill_6_name'),
    level=request.form.get('skill_6_level'),
    char = character.id
    )
    boon_1 = Boon(
    name=request.form.get('boon_1_name'),
    char = character.id
    )
    boon_2 = Boon(
    name=request.form.get('boon_2_name'),
    char = character.id
    )
    boon_3 = Boon(
    name=request.form.get('boon_3_name'),
    char = character.id
    )
    boon_4 = Boon(
    name=request.form.get('boon_4_name'),
    char = character.id
    )
    boon_5 = Boon(
    name=request.form.get('boon_5_name'),
    char = character.id
    )
    bane_1 = Bane(
    name=request.form.get('bane_1_name'),
    char = character.id
    )
    bane_2 = Bane(
    name=request.form.get('bane_2_name'),
    char = character.id
    )
    bane_3 = Bane(
    name=request.form.get('bane_3_name'),
    char = character.id
    )
    bane_4 = Boon(
    name=request.form.get('bane_4_name'),
    char = character.id
    )
    bane_5 = Boon(
    name=request.form.get('bane_5_name'),
    char = character.id
    )
    school = School(
    name=request.form.get('school'),
    level=request.form.get('school_lvl'),
    char = character.id
    )
    prof_1 = Profs(
    name=request.form.get('proficiency_1'),
    char= character.id
    )
    prof_2 = Profs(
    name=request.form.get('proficiency_2'),
    char= character.id
    )
    prof_3 = Profs(
    name=request.form.get('proficiency_3'),
    char= character.id
    )
    talent_1 = Talents(
    name=request.form.get('talent_1'),
    char=character.id
    )
    talent_2 = Talents(
    name=request.form.get('talent_2'),
    char=character.id
    )
    talent_3 = Talents(
    name=request.form.get('talent_3'),
    char=character.id
    )
    talent_4 = Talents(
    name=request.form.get('talent_4'),
    char=character.id
    )
    talent_5 = Talents(
    name=request.form.get('talent_5'),
    char=character.id
    )
    weapon_1 = db.session.query(Weapons).filter(Weapons.name == request.form.get('wep_1_name'))
    weapon_1_char = Weapon_char(
    char=character.id,
    weap_id=weapon_1.id
    )
    weapon_2 = db.session.query(Weapons).filter(Weapons.name == request.form.get('wep_2_name'))
    weapon_2_char = Weapon_char(
    char=character.id,
    weap_id=weapon_2.id
    )
    weapon_3 = db.session.query(Weapons).filter(Weapons.name == request.form.get('wep_3_name'))
    weapon_3_char = Weapon_char(
    char=character.id,
    weap_id=weapon_3.id
    )
    armor_1 = db.session.query(Armour).filter(Armour.name == request.form.get('armor_1_name'))
    armor_1_char = Armour_char(
    char=character.id,
    weap_id=armor_1.id
    )
    armor_2 = db.session.query(Armour).filter(Armour.name == request.form.get('armor_2_name'))
    armor_2_char = Armour_char(
    char=character.id,
    weap_id=armor_2.id
    )
    armor_3 = db.session.query(Armour).filter(Armour.name == request.form.get('armor_3_name'))
    armor_3_char = Armour_char(
    char=character.id,
    weap_id=armor_3.id
    )
    armor_4 = db.session.query(Armour).filter(Armour.name == request.form.get('armor_4_name'))
    armor_4_char = Armour_char(
    char=character.id,
    weap_id=armor_4.id
    )
    armor_5 = db.session.query(Armour).filter(Armour.name == request.form.get('armor_5_name'))
    armor_5_char = Armour_char(
    char=character.id,
    weap_id=armor_5.id
    )
    db.session.add(character)
    db.session.add(skill_1)
    db.session.add(skill_2)
    db.session.add(skill_3)
    db.session.add(skill_4)
    db.session.add(skill_5)
    db.session.add(skill_6)
    db.session.add(boon_1)
    db.session.add(boon_2)
    db.session.add(boon_3)
    db.session.add(boon_4)
    db.session.add(boon_5)
    db.session.add(bane_1)
    db.session.add(bane_2)
    db.session.add(bane_3)
    db.session.add(bane_4)
    db.session.add(bane_5)
    db.session.add(school)
    db.session.add(prof_1)
    db.session.add(prof_2)
    db.session.add(prof_3)
    db.session.add(talent_1)
    db.session.add(talent_2)
    db.session.add(talent_3)
    db.session.add(talent_4)
    db.session.add(talent_5)
    db.session.add(weapon_1_char)
    db.session.add(weapon_2_char)
    db.session.add(weapon_3_char)
    db.session.add(armor_1_char)
    db.session.add(armor_2_char)
    db.session.add(armor_3_char)
    db.session.add(armor_4_char)
    db.session.add(armor_5_char)
    db.session.commit()


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
