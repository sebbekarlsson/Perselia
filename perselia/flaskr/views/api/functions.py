from flask import Blueprint, render_template, abort, request, Response, jsonify
from jinja2 import TemplateNotFound
from api.users import Users


functions = Blueprint('functions', __name__)

valid_classes = [\
    'Users'
]

@functions.route('/api/<function>', methods=['GET', 'POST'])
def call(function):
    klazz = function.split('.')[0].title()

    if klazz in valid_classes:
        return jsonify(getattr(globals()[klazz](), function.split('.')[1])(request.get_json()))
    else:
        abort(403)