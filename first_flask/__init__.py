from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app=Flask(__name__)

    from first_flask.users.views import mod as user_module

    app.register_blueprint(user_module)
    return app










