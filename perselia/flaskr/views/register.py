from flask import Blueprint, render_template, abort, request, Response, session, url_for, redirect
from jinja2 import TemplateNotFound

from flask.ext.wtf import Form
from wtforms import BooleanField, TextField, PasswordField, validators

import requests

import json

from api.functions import JSON_HEADERS


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

    error = None
    form = RegisterForm(request.form, csrf_enabled=False)

    if form.validate_on_submit():
        r = requests.post(
                request.url_root.rstrip('/') + '/api/users.register',
                data=json.dumps
                (
                    {   
                        'users':[
                            {
                                'firstname': form.firstname.data,
                                'lastname': form.lastname.data,
                                'email': form.email.data,
                                'avatar_url': form.avatar_url.data,
                                'password': form.password.data,
                                'password_confirm': form.password_confirm.data,
                                'master': 1
                            }
                        ]
                    }
                ),
                headers=JSON_HEADERS
            )
        _r = json.loads(r.text)
        if _r['errors'] is None:
            r = requests.post(
                request.url_root.rstrip('/') + '/api/users.login',
                data=json.dumps
                (
                    {
                        'email': form.email.data,
                        'password': form.password.data
                    }
                ),
                headers=JSON_HEADERS
            )
        _r = json.loads(r.text)
        if _r['errors'] is None:
            session['user_id'] = _r['user_id']
            
            return redirect('/panel')

        else:
            error = _r['errors']
        

    return render_template('register.html', form=form, error=error)