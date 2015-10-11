from flask import Blueprint, render_template, abort, request, Response, session
from jinja2 import TemplateNotFound

from flask.ext.wtf import Form
from wtforms import BooleanField, TextField, PasswordField


login = Blueprint('login', __name__, template_folder='templates')

class LoginForm(Form):
    email = TextField('Email')
    password = PasswordField('Password')

@login.route('/login', methods=['GET', 'POST'])
def _login():

    form = LoginForm(request.form, csrf_enabled=False)

    if form.validate_on_submit():
        return render_template('sorry.html')
        

    return render_template('login.html', form=form)