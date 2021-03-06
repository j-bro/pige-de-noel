"""
urls.py

URL dispatch route mappings and error handlers

"""
from flask import render_template

from application import app
from application import views


## URL dispatch rules
# App Engine warm up handler
# See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests
app.add_url_rule('/_ah/warmup', 'warmup', view_func=views.warmup)

# Home page
app.add_url_rule('/', 'home', view_func=views.home)

app.add_url_rule('/post_login', 'post_login', view_func=views.post_login)

app.add_url_rule('/create_group', 'create_group', view_func=views.create_group, methods=['GET', 'POST'])

app.add_url_rule('/manage_group', 'manage_group', view_func=views.manage_group)

app.add_url_rule('/exchange', 'exchange', view_func=views.exchange)

app.add_url_rule('/account_settings', 'account_settings', view_func=views.account_settings, methods=['GET', 'POST'])

app.add_url_rule('/logout', 'logout', view_func=views.logout)


# Contrived admin-only view example
# app.add_url_rule('/admin_only', 'admin_only', view_func=views.admin_only)

app.add_url_rule('/admin_only', 'admin_only', view_func=views.admin_only)

## Error handlers
# Handle 404 errors
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Handle 500 errors
@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

