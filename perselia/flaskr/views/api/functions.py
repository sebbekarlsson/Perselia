from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from api.users import Users


functions = Blueprint('functions', __name__)

valid_classes = [\
    'Users'
]

@functions.route('/api/<function>')
def call(function):
    if function.split('.')[0].title() in valid_classes:
        return getattr(globals()[function.split('.')[0].title()](), function.split('.')[1])()
    else:
        abort(403)