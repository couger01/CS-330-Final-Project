from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)

class User:
    def __init__(self):
        self.is_authenticated = True
        self.email = 'test@gmail.com'

@app.route("/")
def main_page():
    u = User()
    upstr = """
            Lorem ipsum dolor sit amet, consectetur adipiscing
            elit. Vivamus eu odio sit amet nibh consequat
            consequat. Etiam et lectus nibh. Fusce quis placerat
            libero. Aliquam interdum mattis ipsum id dictum. Donec
            consequat scelerisque risus vel consequat. Integer eget
            libero eleifend mauris imperdiet vehicula eu sit amet
            erat. Aenean mauris lacus, dignissim sit amet metus
            eget, pharetra semper purus. Donec quis viverra nulla.
            Fusce nec urna neque. Fusce tincidunt dolor eget libero
            mattis consectetur.
            """
    up = [upstr for k in range(5)]
    return render_template("main_page.html", user=u, updates=up)


@app.route("/search")
def results_page():
    u = User()
    res = [[3, "Ashleigh", "Adelaide the Mercenary"],
           [1, "Eric", "Phillip the Bastard"],
           [5, "Ashleigh", "Anna the Knight"],
           [7, "Anonymous", "Mildred the Surgeon"]]
    return render_template("search_results.html", user=u, results=res)


@app.route("/view")
def view_page():
    u = User()
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

    return render_template("char_view_page.html", user=u, character=char)


if __name__ == '__main__':
    app.run(debug=True)
