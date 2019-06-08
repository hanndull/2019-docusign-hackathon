from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
db = SQLAlchemy(app)

class User(db.Model):
    """Users table"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    is_ranger = db.Column(db.Boolean, default=False, nullable=True)

    user_forms = db.relationship("ActivityForms", secondary="associated_forms", 
                                    backref="users")

    def __repr__(self):
        """ String representation of object """

        return f'<User id = {id}, ranger = {is_ranger}, email = {email}>'

class ActivityForms(db.Model):
    """Activity form table"""

    __tablename__ = "activity_forms"

    form_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    form_name = db.Column(db.String(100), nullable=False)
    geolocation = db.Column(db.String(200), nullable=False)


    def __repr__(self):
        """ String representation of object """

        return f'<Form id="{form_id}", form_name={form_name}, geoloc={geolocation}>'

class AssociatedForm(db.Model):
    """ User-Activity Form Association table """

    __tablename__ = "associated_forms"

    user_act_form_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    form_id = db.Column(db.Integer, db.ForeignKey('form_id'), nullable=False)
    is_completed = db.Column(db.Boolean, default=False, nullable=True)

    def __repr__(self):
        """ String representation of object """

        return f'''<Associated form id={user_act_form_id}, user_id={user_id}, 
                        form_id={form_id}, comp?={is_completed}>'''


def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our PostgreSQL database

    #Configure database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///docusign' 
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # leave in a state of being able to work with the database directly

    from server import app
    connect_to_db(app)
    db.create_all()
    print("Connected to DB.")

