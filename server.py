from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session, jsonify
from model import User, Message, Conversation, User_conv, db, connect_to_db

app = Flask(__name__)
# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"
# Raise error for undefined variable
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def register():
    """My login page."""

    return render_template('login.html')


@app.route('/register_confirm', methods=["POST"])
def register_confirm():
    """Registration confirmation page."""

    email = request.form.get("email")

    #add the user to the session
    session['email'] = email

    #add the user to the db
    new_user = User(email=email)

    db.session.add(new_user)
    db.session.commit()

    return render_template('register_confirm.html', user_email=session['email'])


@app.route('/add_message', methods=["POST"])
def add_message():
    """Add messages to message log"""

    message = request.form.get("message")

    #get the user's id
    user = User.query.filter(User.email == session['email']).first()

    #add the message to the db
    message = Message(content=message, user_id=user.user_id)

    db.session.add(message)
    db.session.commit()

    #collect all messages from the db
    messages = Message.query.all()

    return render_template('register_confirm.html', user_email=session['email'])


#------------------------------------------

if __name__ == "__main__":
    app.debug = True
    app.jinja_env.auto_reload = app.debug  # make sure templates, etc. are not cached in debug mode

    connect_to_db(app, 'postgresql:///chatappdb')

    app.run(port=5000, host='0.0.0.0')
