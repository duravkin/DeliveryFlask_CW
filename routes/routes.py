from flask import Blueprint, render_template, send_file
from functions.create_docx import generate_order_report

main_routes = Blueprint('main', __name__)


@main_routes.route('/')
def index():
    return render_template('index.html')


@main_routes.route('/generate_report/docx/<int:report_id>')
def generate_report(report_id):
    filepath = generate_order_report(report_id)
    return send_file(
        filepath,
        as_attachment=True,  # Указывает, что файл должен быть загружен
        download_name=f"report_{report_id}.docx",  # Имя файла для пользователя
        mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
    )
