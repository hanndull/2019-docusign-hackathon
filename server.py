
##### Project Info ############################################################

    ### https://github.com/hanndull/2019-docusign-hackathon
    ### DocuSign Hackathon 2019, https://2019-ds-momentum-hackathon.devpost.com/

##### Import Libraries #######################################################

from jinja2 import StrictUndefined
from flask import Flask, render_template, redirect, request, flash, session, jsonify
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, ### TODO - insert classes from model
from sqlalchemy import func, distinct
import requests
import json

##### Create App #############################################################

app = Flask(__name__)

app.secret_key = "forests"

### Raise an error for an undefined variable in Jinja
app.jinja_env.undefined = StrictUndefined

##### Define Routes ##########################################################

@app.route('/')
def show_homepage():
    """Display home page"""
    
    pass


##### Dunder Main ############################################################

if __name__ == "__main__":
    
    ### debug must be True at time DebugToolbarExtension invoked
    app.debug = True
    
    ### ensures templates, etc. are not cached in debug mode
    app.jinja_env.auto_reload = app.debug


    connect_to_db(app)

    ### enables use of DebugToolbar
    DebugToolbarExtension(app)
    # import pdb; pdb.set_trace()
    app.run(port=5000, host='0.0.0.0')