from flask import Blueprint, jsonify, request, redirect, url_for

A = Blueprint('user', __name__)


@A.route('/welcome')
def welcome():
    return "WELCOME TO MY creator WEBPAGE"


@A.route('/admin1')
def admin():
    return 'hello admin welcome to pune'


@A.route('/guest1/<guestname>')
def hello_guest(guestname):
    return 'hello guest welcome to pune'


@A.route('/user1/<name>')
def hello_user(name):
    if name == hello_guest:
        return redirect(url_for('hello_guest'))
    else:
        return redirect(url_for('admin'))
