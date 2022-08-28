from flask import Flask


def create_app():
    app=Flask(__name__)

    from second_flask.users.views import A as user_module

    app.register_blueprint(user_module)
    return app