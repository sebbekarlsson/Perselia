from flask import Blueprint, render_template, abort, request, Response, jsonify
from jinja2 import TemplateNotFound
from api.users import Users
from api.functions import ok, errors


functions = Blueprint('functions', __name__)

valid_classes = [\
    'Users'
]

token = '873hajhshgab927Jj1wxy0'

@functions.route('/api/<function>', methods=['GET', 'POST'])
def call(function):

    if request.method == 'GET':
        return jsonify(errors(['perselia/flaskr/api/errors/bad_request.json']))

    klazz = function.split('.')[0].title()

    if klazz in valid_classes:
        return jsonify(getattr(globals()[klazz](), function.split('.')[1])(data=request.get_json(), token=token))
    else:
        abort(403)