from flask import jsonify
import json as json


def throw_error(status, error):
    response = {
            'status': status,
            'errors': error
    }

    return response