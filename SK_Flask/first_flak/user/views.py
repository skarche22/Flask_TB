from flask import Blueprint

mod= Blueprint('user',__name__,url_prefix='/user')

@mod.route('/')
def home():
    return 'my sweet home'


