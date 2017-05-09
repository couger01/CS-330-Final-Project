from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


class User:
    def __init__(self, name="Anonymous", logged_in=False):
        self.name = name
        self.logged_in = logged_in


@app.route("/")
def main_page():
    u = User()
    return render_template("main_page.html", user=u)


@app.route("/search")
def results_page():
    u = User()
    res = [[3, "Ashleigh", "Adelaide the Mercenary"],
           [1, "Eric", "Phillip the Bastard"],
           [5, "Ashleigh", "Anna the Knight"],
           [7, "Anonymous", "Mildred the Surgeon"]]
    return render_template("search_results.html", user=u, results=res)


if __name__ == '__main__':
    app.run(debug=True)
