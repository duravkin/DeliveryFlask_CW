from flask import Blueprint, render_template

main_routes = Blueprint('main', __name__)


@main_routes.route('/')
def index():
    return render_template('index.html')

# @main_routes.route('/reports')
# def reports():
#     return render_template('reports.html')