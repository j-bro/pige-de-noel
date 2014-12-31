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
from forms import ExampleForm
from models import ExampleModel


# Flask-Cache (configured to use App Engine Memcache API)
cache = Cache(app)


def home():
    return render_template("home.html")

def group_management():
    return render_template("group_management.html")

def participant_view():
    return render_template("participant_view.html")

@admin_required
def admin_only():
    """This view requires an admin account"""
    return 'Super-seekrit admin page.'

def warmup():
    """App Engine warmup handler
    See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests

    """
    return ''

