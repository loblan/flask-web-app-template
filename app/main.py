from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def hello_world():
    return "Hello World!"

@main.route('/<path>')
def welcome_path(path):
    return "Welcome to {}!".format(path)

@main.route('/template')
def template_example():
    list = [ 'One','Two','Three' ]
    return render_template('example.html', title='Template', list=list)