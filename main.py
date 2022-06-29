from flask import Flask
from database import db
from routes.products import product_blueprint
from schema import marshamllow


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    app.register_blueprint(product_blueprint)
    marshamllow.init_app(app)
    db.init_app(app)
    return app


# Run Server
if __name__ == '__main__':
    server = create_app()
    server.run(debug=True)
