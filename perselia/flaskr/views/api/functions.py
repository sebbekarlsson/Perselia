from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from api.users import Users


functions = Blueprint('functions', __name__)

@functions.route('/api/<function>')
def call(function):
    return getattr(globals()[function.split('.')[0].title()](), function.split('.')[1])()