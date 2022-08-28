from flask import Flask

def create_app():
    app = Flask(__name__)
    # app.config['SECTRET_KEY']='SANTOSH'

    from first_flak.user.views import mod as user_module

    app.register_blueprint(user_module)
    return app