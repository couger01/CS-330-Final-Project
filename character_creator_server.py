from flask import Flask, render_template, redirect, url_for, request, Response
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required, utils, LoginForm, core
from flask_bootstrap import Bootstrap
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
    reach = db.Column(db.String(1))
    swing = db.Column(db.String(255))
    thrust = db.Column(db.String(255))
    defense_guard = db.Column(db.String(255))
    special = db.Column(db.String(255))
    weight = db.Column(db.Integer)
    cost = db.Column(db.Integer)
    weapChar = db.relationship("Weapon_char")

class Armour(db.Model):
    __tablename__ = 'armour'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    AVC = db.Column(db.Integer)
    AVP = db.Column(db.Integer)
    AVB = db.Column(db.Integer)
    coverage = db.Column(db.String(255))
    special = db.Column(db.String(255))
    weight = db.Column(db.Integer)
    cost = db.Column(db.Integer)
    armourChar = db.relationship("Armour_char")

class Armour_char(db.Model):
    __tablename__ = 'armour_char'
    id = db.Column(db.Integer, primary_key=True)
    char = db.Column(db.Integer, db.ForeignKey('characters.id'))
    armor_id = db.Column(db.Integer, db.ForeignKey('armour.id'))

class Boons(db.Model):
    __tablename__ = 'boons'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    cost = db.Column(db.Integer)
    char = db.Column(db.Integer, db.ForeignKey('characters.id'))

class Banes(db.Model):
    __tablename__ = 'banes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    cost = db.Column(db.Integer)
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

class Talents(db.Model):
    __tablename__ = 'talents'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    char = db.Column(db.Integer, db.ForeignKey('characters.id'))



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
    print(fc_skills[0].name)
    print(fc.name)
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

@app.route('/api/weapons/?q=<name>', methods=['GET'])
def get_weapon(name):
    weapons_list = []
    weapons = db.session.query(Weapons).filter(Weapons.name.like(name)).all()
    for weapon in weapons:
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
    print(weapons_list)
    return weapons_list

@app.route('/api/armors/?q=<name>',methods=['GET'])
def get_armor(name):
    armors_list = []
    armors = db.session.query(Armours).filter(Armours.name.like(name)).all()
    for armor in armors:
        armor_list = []
        armor_list.append(armor.name)
        armor_list.append(armor.AVC)
        armor_list.append(armor.AVP)
        armor_list.append(armor.AVB)
        armor_list.append(armor.coverage)
        armor_list.append(armor.weight)
        armor_list.append(armor.special)
        armors_list.append(armor_list)

    return armors_list


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
