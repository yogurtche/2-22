from flask import Blueprint, render template


course = Blueprint('course', __name__, template_folder='template')


course_list = ['MAT456', 'COS160', 'INF100', 'BUS300', 'JMC200']


@course.route('/')
def show():
    return render_template('index.html', course=course_list)
