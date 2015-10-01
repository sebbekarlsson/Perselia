from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from api.users import Users


functions = Blueprint('functions', __name__)

valid_classes = [\
    'Users'
]

@functions.route('/api/<function>')
def call(function):
    klazz = function.split('.')[0].title()

    if klazz in valid_classes:
        return getattr(globals()[klazz](), function.split('.')[1])()
    else:
        abort(403)