import sys
from flask import Flask
from flask import render_template
from flask_frozen import Freezer

FREEZER_DESTINATION = 'docs'
URL_EASYCHAIR_SUBMISSION = 'https://easychair.org/conferences/?conf=ieeeichi2022'

app = Flask(__name__)
app.config.from_object(__name__)
freezer = Freezer(app)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/call_for_sponsors.html")
def call_for_sponsors():
    return render_template('call_for_sponsors.html')


@app.route("/call_for_contributions.html")
def call_for_contributions():
    return render_template('call_for_contributions.html')


@app.route("/call_for_papers.html")
def call_for_papers():
    return render_template('call_for_papers.html')


@app.route("/call_for_posters_and_demos.html")
def call_for_posters_and_demos():
    return render_template('call_for_posters_and_demos.html')


@app.route("/call_for_workshops.html")
def call_for_workshops():
    return render_template('call_for_workshops.html')


@app.route("/call_for_doctorial_consortium.html")
def call_for_doctorial_consortium():
    return render_template('call_for_doctorial_consortium.html')


@app.route("/call_for_industry_track.html")
def call_for_industry_track():
    return render_template('call_for_industry_track.html')


@app.route("/call_for_tutorials.html")
def call_for_tutorials():
    return render_template('call_for_tutorials.html')


@app.route("/attending.html")
def attending():
    return render_template('attending.html')


@app.route("/program.html")
def program():
    return render_template('program.html')


@app.route("/keynotes.html")
def keynotes():
    return render_template('keynotes.html')


@app.route("/committees.html")
def committees():
    return render_template('committees.html')


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
        print('* built static version by Flask-Freezer')
    else:
        app.run(host='0.0.0.0', debug=True)