from flask import Flask
from views.api.functions import functions
from views.index import index
from models import initialize_database


app = Flask(__name__)
app.register_blueprint(functions)
app.register_blueprint(index)

@app.route("/")
def hello():
    return "main page"

if __name__ == "__main__":
    initialize_database()
    app.run(debug=True)