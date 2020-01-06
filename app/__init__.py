from flask import Flask, render_template, redirect, flash, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

from .config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
login = LoginManager(app)
Bootstrap(app)

# import down here because the models file requires the db object to be created
from .models import User
from .forms import LoginForm, RegistrationForm
from app.blueprints.blog import blog
from app.blueprints.mcserver import mcserver

# register blueprints
app.register_blueprint(mcserver, url_prefix='/mcserver')
app.register_blueprint(blog, url_prefix='/blog')

# set login view for login_required decorators
login.login_view = 'login'


@app.route("/")
@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    # don't bother with login page if user is already logged in
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password!')
            return redirect(url_for('login'))

        # remember me is false for development
        login_user(user, remember=False)
        # if player was trying to access a different page
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now registered')
        return redirect(url_for('login'))

    return render_template('register.html', title='Register', form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route("/cloud")
def cloud():
    return redirect('https://cloud.scottcorbat.com')


@app.route("/quotes1984")
def quotes1984():
    return render_template('quotes1984.html')


@app.route("/quotesBNW")
def quotesBNW():
    return render_template('quotesBNW.html')


@app.route("/about")
def about():
    return render_template('about.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/legacy")
def legacy():
    return render_template('legacy.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080', debug=True)
