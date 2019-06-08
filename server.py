
##### Project Info ############################################################

    ### https://github.com/hanndull/2019-docusign-hackathon
    ### DocuSign Hackathon 2019, https://2019-ds-momentum-hackathon.devpost.com/

##### Import Libraries #######################################################

from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
# from model import connect_to_db, db, ### TODO - insert classes from model
from sqlalchemy import func, distinct
import requests

##### Create App #############################################################

app = Flask(__name__)

app.secret_key = "forests"

### Raise an error for an undefined variable in Jinja
app.jinja_env.undefined = StrictUndefined

##### Define Routes ##########################################################

@app.route('/')
def show_homepage():
    """Display home page"""
    
    return render_template('homepage.html')

@app.route('/login')
def user_login():
    """Display user login page"""

    return render_template('login.html')

@app.route('/handle_login')
def handle_login():
    """Handle user login"""

    first_name = request.args.get('first-name')
    last_name = request.args.get('last-name')
    email = request.args.get('email')
    user_type = request.args.get('type')

    if user_type != 'ranger':

        is_user = db.session.query(User.email).filter(User.email == email).first()

        if is_user:
            return redirect('/activities', name = first_name)

        else: 
            return redirect('/register')

    else:
        return redirect('/')

@app.route('/register')
def user_registration():
    """Register user"""

    return render_template('registration.html')

@app.route('/handle_registration', methods=["POST"])
def handle_registration():
    """Handle user registration"""

    first_name = request.form.get('first-name')
    last_name = request.form.get('last-name')
    email = request.form.get('email')
    user_type = request.form.get('type')

    if user_type == 'ranger':
        is_ranger = True
    else:
        is_ranger = False

    user = db.session.add(User(first_name, last_name, email, is_ranger))
    db.session.commit()

    return redirect('/login')

##### Dunder Main ############################################################

if __name__ == "__main__":
    
    ### debug must be True at time DebugToolbarExtension invoked
    app.debug = True
    
    ### ensures templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug


    # connect_to_db(app)

    ### enables use of DebugToolbar
    DebugToolbarExtension(app)
    # import pdb; pdb.set_trace()
    app.run(port=5000, host='0.0.0.0')