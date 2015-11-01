from flask import Blueprint, render_template, abort, request, Response, session, redirect
from jinja2 import TemplateNotFound


logout = Blueprint('logout', __name__, template_folder='templates')


@logout.route('/logout', methods=['GET', 'POST'])
def _logout():
    if 'user_id' in session:
        del session['user_id']
        
    return redirect('/')
    