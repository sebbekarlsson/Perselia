from flask import Blueprint, render_template, abort, request, Response, session
from jinja2 import TemplateNotFound


panel = Blueprint('panel', __name__, template_folder='templates')


@panel.route('/panel', methods=['GET', 'POST'])
def _panel():
    return render_template('panel.html')
    