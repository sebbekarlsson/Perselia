from flask import Blueprint, render_template, abort, request, Response
from jinja2 import TemplateNotFound


index = Blueprint('index', __name__, template_folder='templates')

token = '873hajhshgab927Jj1wxy0'

@index.route('/', methods=['GET', 'POST'])
def _index():
    return render_template('index.html')
    