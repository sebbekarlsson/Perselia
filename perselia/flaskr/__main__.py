from flask import Flask, request
from models import initialize_database, create_admin
from flask.ext.cors import CORS


app = Flask(__name__)
CORS(app)

app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

''' API functions blueprint '''
from views.api.functions import functions
app.register_blueprint(functions)

''' index blueprint '''
from views.index import index
app.register_blueprint(index)

''' register blueprint '''
from views.register import register
app.register_blueprint(register)

''' login blueprint '''
from views.login import login
app.register_blueprint(login)

''' logout blueprint '''
from views.logout import logout
app.register_blueprint(logout)

''' panel blueprint '''
from views.panel import panel
app.register_blueprint(panel)


if __name__ == "__main__":
    initialize_database()
    app.run(debug=True, threaded=True)