from django import template
from django.template.loader import get_template

register = template.Library()

def my_template(value, arg):
    if arg == 'change':
        value = 'Rahim'
        return value
    if arg == 'title':
        return value.title()

def show_courses():
    courses = [
        {
            'id': 1,
            'course': 'C',
            'teacher': 'Abdullah'
        },
        {
            'id': 2,
            'course': 'C++',
            'teacher': 'Al'
        },
        {
            'id': 3,
            'course': 'Python',
            'teacher': 'Towsif'
        }
    ]
    return {'courses': courses}
courses_template = get_template('first_app/courses.html')
register.filter('change_name', my_template)
register.inclusion_tag(courses_template)(show_courses)