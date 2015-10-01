from flask import Flask
from views.api.functions import functions


app = Flask(__name__)
app.register_blueprint(functions)

@app.route("/")
def hello():
    return "main page"

if __name__ == "__main__":
    app.run(debug=True)