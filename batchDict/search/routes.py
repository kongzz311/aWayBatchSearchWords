from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from batchDict.search.forms import SearchForm

search = Blueprint('search', __name__)


@search.route('/search', methods=['POST', 'GET'])
def do_search():
    form = SearchForm()
    return render_template('create_post.html', title='批量查找', form=form, legend='批量查找')
