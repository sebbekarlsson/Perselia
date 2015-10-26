from flask import jsonify
import json as json


def throw_error(status, errors):
    response = {
            'status': status,
            'errors': [errors]
    }

    return response