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

@app.route("/mcserver")
def mcserver():
    return render_template('mcserver.html')

@app.route("/quotes1984")
def quotes1984():
    return render_template('quotes1984.html')

@app.route("/quotesBNW")
def quotesBNW():
    return render_template('quotesBNW.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/legacy")
def legacy():
    return render_template('legacy.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080', debug=True)
