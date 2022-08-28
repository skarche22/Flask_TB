from flask import Flask

Pune=Flask(__name__)


@Pune.route('/')
def welcome():
    return 'welcome to pune'

@Pune.route('/Goa')            ##http://127.0.0.1:5000/Goa/   then error will shown As 404 (NOT FOUND)
def welcome_Goa():
    return 'welcome to Goa SINGHAM'

@Pune.route('/cap/<name>')
def capital(name):
    return 'the capital of my state is: %s' %name

@Pune.route('/calc/<int:num>')
def calc(num):
    return 'number is %d'%num


if __name__=='__main__':
    Pune.run(debug=True)