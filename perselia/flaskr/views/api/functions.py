from flask import Blueprint, render_template, abort, request, Response, jsonify
from jinja2 import TemplateNotFound
from api.users import Users
from api.errors import throw_error
from flask.ext.cors import CORS


functions = Blueprint('functions', __name__)

CORS(functions)

valid_classes = [\
    'Users'
]

token = '873hajhshgab927Jj1wxy0'

@functions.route('/api/<function>', methods=['GET', 'POST'])
def call(function):

    if request.method == 'GET':
        response_object = throw_error(400, 'GET is not allowed')
        result = jsonify(response_object)
        result.status_code = response_object['status']

        return result

    klazz = function.split('.')[0].title()

    if klazz in valid_classes:
        response_object = getattr(globals()[klazz](), function.split('.')[1])(data=request.get_json(), token=token)
        result = jsonify(response_object)
        result.status_code = response_object['status']

        return result

    else:
        abort(403)