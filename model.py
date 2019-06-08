from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
db = SQLAlchemy(app)

class User():
    """Users table"""

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(100), nullable=True)
    is_ranger = db.Column(db.Boolean, default=False, nullable=True)





if __name__ == "__main__":
    app.debug = False

    from server import app
    connect_to_db(app)
    print("Connected to DB.")

