from flask import Flask, render_template, redirect
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/cloud")
def cloud():
    return redirect('https://cloud.scottcorbat.com')

@app.route("/quotes")
def quotes():
    return render_template('quotes.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/legacy")
def legacy():
    return render_template('legacy.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080', debug=True)
