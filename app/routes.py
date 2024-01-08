from flask import render_template, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user
from app import app, db
from app.models import User
from app.forms import LoginForm, ShortLinkForm
from app.models import ShortLink
# app/routes.py
from app.utils import generate_unique_short_code


from app.models import ShortLink, LinkAnalytics
from flask_login import current_user, login_required
# Define routes here

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/create_short_link', methods=['GET', 'POST'])
def create_short_link():
    form = ShortLinkForm()

    if form.validate_on_submit():
        # Generate a unique short code (you may use a library for this)
        short_code = generate_unique_short_code()


        # Create a ShortLink object and save it to the database
        short_link = ShortLink(original_url=form.original_url.data, short_code=short_code)
        db.session.add(short_link)
        db.session.commit()

        # Redirect to a page displaying the short link
        return render_template('short_link_created.html', short_link=short_link)

    return render_template('create_short_link.html', form=form)

@app.route('/analytics')
@login_required
def analytics():
    # Retrieve short links created by the current user
    user_short_links = ShortLink.query.filter_by(user_id=current_user.id).all()

    # Display analytics for each short link
    return render_template('analytics.html', user_short_links=user_short_links)