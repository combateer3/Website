from flask import Blueprint, render_template

mcserver = Blueprint('mcserver', __name__, template_folder='templates')


@mcserver.route('/')
def mcserver_home():
    return render_template('mcserver.html')


@mcserver.route('/admin')
def mcadmin():
    return render_template('mcadmin.html')


@mcserver.route('/moderator')
def mcmod():
    return render_template('mcmoderator.html')


@mcserver.route('/member')
def mcmember():
    return render_template('mcmember.html')
