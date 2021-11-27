'''
Web application homepage views used

'''

from flask import Blueprint, Flask, render_template

home_page = Blueprint('home_page', __name__, template_folder='templates')


@home_page.route("/")
@home_page.route("/home")
def show_home():
    '''
    Function is used to show user the home page

    '''
    return render_template('home.html')

