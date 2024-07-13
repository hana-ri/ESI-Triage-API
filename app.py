# Importing the necessary modules and libraries
from flask import Flask
from routes.blueprint import blueprint

def create_app():
    app = Flask(__name__)  # flask app object
    return app

app = create_app()  # Creating the app

app.register_blueprint(blueprint, url_prefix='/')

if __name__ == '__main__':  # Running the app
    app.run(host='127.0.0.1', port=5000, debug=True)
