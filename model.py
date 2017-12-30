from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """Users of my website."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(40), nullable=False)
    password = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "< User name: {} >".format(self.name)


class Message(db.Model):
    """Articles from rss feeds of blogs that my users follow."""

    __tablename__ = "messages"

    message_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    conversation_id = db.Column(db.Integer, db.ForeignKey('conversations.conversation_id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    publish_date = db.Column(db.DateTime, nullable=False)
    content = db.Column(db.String(10000), nullable=True)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "< Message author: {} >".format(self.author)


class Conversation(db.Model):
    """Favorited articles of my users."""

    __tablename__ = "conversations"

    conversation_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<Conversation name: {}>".format(self.name)


class User_conv(db.Model):
    """Association table between users and blogs."""

    __tablename__ = "user_convs"

    user_conv_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    conversation_id = db.Column(db.Integer, db.ForeignKey('conversations.conversation_id'), nullable=False)

    # Define relationship to user
    user = db.relationship("User", backref='user_convs')

    # Define relationship to blog
    conversation = db.relationship("Conversation", backref='user_convs')

    def __repr__(self):
        """Provide helpful representation when printed."""

        return "<User-conv User: {} Conversation: {}>".format(self.user.name, self.conversation.name)


#-----------------------------------------


def connect_to_db(app, db_uri):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    # So that we can use Flask-SQLAlchemy, we'll make a Flask app
    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app, 'postgresql:///chatappdb')
