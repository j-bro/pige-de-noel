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


# Flask-Cache (configured to use App Engine Memcache API)
cache = Cache(app)


def home():
    if users.get_current_user():
        return redirect('participant_view')
    return render_template("home.html", user=users.get_current_user())

@login_required
def post_login():
    # Sets the "global" user variable NOT WORKING
    #g.user = users.get_current_user()
    return redirect(request.args.get('r'))

@login_required
def manage_group():
    return render_template("manage_group.html", user=users.get_current_user())

@login_required
def participant_view():
    return render_template("participant_view.html", user=users.get_current_user())

@login_required
def create_group():
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

