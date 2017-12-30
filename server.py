from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session, jsonify

app = Flask(__name__)
# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"
# Raise error for undefined variable
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def login():
    """ My login page."""

    return render_template('login.html')


#------------------------------------------

if __name__ == "__main__":
    app.debug = True
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    #connect_to_db(app, 'postgresql:///projectdb')

    app.run(port=5000, host='0.0.0.0')
