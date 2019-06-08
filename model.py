from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap

app = Flask(__name__)
db = SQLAlchemy(app)




if __name__ == "__main__":
    app.debug = False



