from flask import Flask, render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def main_page():
    u = {'logged_in': False, 'name': 'Anonymous'}
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
    u = {'logged_in': False, 'name': 'Ashleigh'}
    res = [[3, "Ashleigh", "Adelaide the Mercenary"],
           [1, "Eric", "Phillip the Bastard"],
           [5, "Ashleigh", "Anna the Knight"],
           [7, "Anonymous", "Mildred the Surgeon"]]
    return render_template("search_results.html", user=u, results=res)


if __name__ == '__main__':
    app.run(debug=True)
