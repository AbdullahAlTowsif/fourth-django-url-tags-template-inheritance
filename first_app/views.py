from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, './first_app/index.html', {"name": "I am Towsif", "marks": 89, "courses": [
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
    ]})
    
def about(request):
    return render(request, './first_app/about.html')