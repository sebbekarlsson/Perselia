from flask import Blueprint, render_template, abort, request, Response, session, url_for, redirect
from jinja2 import TemplateNotFound

from flask.ext.wtf import Form
from wtforms import BooleanField, TextField, PasswordField, validators

import requests

import json

from api.functions import JSON_HEADERS


login = Blueprint('login', __name__, template_folder='templates')

class LoginForm(Form):
    email = TextField('Email', [validators.Required()])
    password = PasswordField('Password', [validators.Required()])

@login.route('/login', methods=['GET', 'POST'])
def _login():

    error = None
    form = LoginForm(request.form, csrf_enabled=False)

    if form.validate_on_submit():
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

    return render_template('login.html', form=form, error=error)