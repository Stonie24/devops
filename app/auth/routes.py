"""
Contains routes used for authenticating User
"""
from urllib.parse import urlparse

from flask import render_template, redirect, url_for, flash, request, current_app
from flask_login import login_user, logout_user, current_user
from prometheus_client import Counter
from app import db
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm
from app.models import User



@bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    Route for registering a user
    """
    if current_user.is_authenticated:
        current_app.logger.debug(f"{current_user} is already registered")
        return redirect(url_for('main.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        current_app.logger.info(f"Registered user {user}")
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title='Register', form=form)



@bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    Route for logging in
    """
    if current_user.is_authenticated:
        current_app.logger.debug(f"{current_user} is already authenticated")
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit(): # if form is valid
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data): # if user exist and passowrd correct
            current_app.logger.info(f"{user} failed login")
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or urlparse(next_page).netloc != '': # if next argument sent. From @login_required
            next_page = url_for('main.index')
        current_app.logger.debug(f"Next from login {next_page}")
        return redirect(next_page)
    return render_template('auth/login.html', title='Sign In', form=form)



@bp.route('/logout')
def logout():
    """
    Route for logging out a user
    """
    current_app.logger.debug(f"{current_user} loged out")
    logout_user()
    return redirect(url_for('main.index'))

ERROR_COUNT = Counter(
    "flask_http_request_errors_total",
    "Total number of HTTP errors",
    ["endpoint"]
)

@bp.route('/trigger-error')
def trigger_error():
    """Trigger an error to test monitoring"""
    ERROR_COUNT.labels(endpoint="/trigger-error").inc()
    raise RuntimeError("Test error to trigger monitoring alerts")
