"""
views.py

URL route handlers

Note that any handler params must match the URL route params.
For example the *say_hello* handler, handling the URL route '/hello/<username>',
  must be passed *username* as the argument.

"""
from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError

from flask import request, render_template, flash, url_for, redirect

from flask_cache import Cache

from application import app
from decorators import login_required, admin_required

from models import User


# Flask-Cache (configured to use App Engine Memcache API)
cache = Cache(app)


def home():
    if users.get_current_user():
        return redirect('exchange')
    return render_template("home.html", user=users.get_current_user())

@login_required
def post_login():
    # Go back home if not logged in
    g_user = users.get_current_user()
    if not g_user:
        return redirect(url_for('home'))
    # if new user, add to db
    existing_user_query = Users.query(Users.user_id == g_user.user_id()).get()
    if not existing_user_query:
        new_user = User(user_id=g_user.user_id(), name=g_user.nickname(), email=g_user.email())
        new_user.put()
    return redirect(request.args.get('r'))

@login_required
def accept_invitation():
    pass

@login_required
def account_settings():
    if request.method == 'POST':
        pass
    
    return render_template("account_settings.html", user=users.get_current_user())

@login_required
def manage_group():
    return render_template("manage_group.html", user=users.get_current_user())

@login_required
def exchange():
    return render_template("exchange.html", user=users.get_current_user())

@login_required
def create_group():
    if request.method == 'POST':
        request.form.get('')
    else:
        return render_template("create_group.html", user=users.get_current_user())

def logout():
    if users.get_current_user():
        return redirect(users.create_logout_url(url_for('home')))

    
@admin_required
def admin_only():
    """This view requires an admin account"""
    return 'Super-seekrit admin page.'

def warmup():
    """App Engine warmup handler
    See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests

    """
    return ''

