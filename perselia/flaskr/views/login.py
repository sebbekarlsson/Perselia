from flask import Blueprint, render_template, abort, request, Response, session
from jinja2 import TemplateNotFound


login = Blueprint('login', __name__, template_folder='templates')


@login.route('/login', methods=['GET', 'POST'])
def _login():
    return render_template('login.html')
    