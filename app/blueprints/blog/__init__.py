from flask import Blueprint, render_template, redirect, url_for
from flask_login import current_user, login_required
from app import db
from app.forms import PostForm
from app.models import Post

blog = Blueprint('blog', __name__, template_folder='templates')


@blog.route('/')
@login_required
def blog_home():
    posts = Post.query.all()
    return render_template('blog.html', posts=posts)


@blog.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, body=form.post.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('blog.blog_home'))

    return render_template('create_post.html', form=form)
