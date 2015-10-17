from flask import Blueprint, render_template, abort, request, Response, session, url_for
from jinja2 import TemplateNotFound

from flask.ext.wtf import Form
from wtforms import BooleanField, TextField, PasswordField, validators


register = Blueprint('register', __name__, template_folder='templates')

class RegisterForm(Form):
    firstname = TextField('Firstname', [validators.Length(min=4, max=25)])
    lastname = TextField('Lastname', [validators.Length(min=4, max=25)])
    email = TextField('Email', [validators.Length(min=6, max=35)])
    avatar_url = TextField('Avatar Url')
    password = PasswordField('Password', [
        validators.Required(),
        validators.EqualTo('password_confirm', message='Passwords must match')
    ])
    password_confirm = PasswordField('Repeat Password')

@register.route('/register', methods=['GET', 'POST'])
def _register():
    form = RegisterForm(request.form, csrf_enabled=False)

    if form.validate_on_submit():
        return render_template('sorry.html')
        

    return render_template('register.html', form=form)