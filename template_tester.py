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


if __name__ == '__main__':
    app.run(debug=True)
