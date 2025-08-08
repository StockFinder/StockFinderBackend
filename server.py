import os

import flask
from flask_cors import CORS

from routing.products_routing import products_routing_blueprint

SECRET_KEY = os.environ.get("FLASK_AUTH_SECRET")


app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.config["SECRET_KEY"] = SECRET_KEY
# CORS(app)

spams = {}
app.register_blueprint(products_routing_blueprint, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
