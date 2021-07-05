from flask import render_template, url_for, flash, redirect, request, abort, Blueprint

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    return redirect(url_for('search.do_search'))


@main.route('/about')
def about():
    return render_template('about.html', title='About')



