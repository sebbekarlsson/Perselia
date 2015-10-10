from flask import Flask
from models import initialize_database


app = Flask(__name__)

''' API functions blueprint '''
from views.api.functions import functions
app.register_blueprint(functions)

''' index blueprint '''
from views.index import index
app.register_blueprint(index)


''' login blueprint '''
from views.login import login
app.register_blueprint(login)


if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)