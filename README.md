# Django Template Inheritance and URL Tags

## Template Inheritance
Django provides a powerful way to reuse HTML structures using **template inheritance**. This allows you to define a base template and extend it in child templates, making your code more maintainable.

### How It Works
1. **Create a Base Template** (e.g., `base.html`):
   ```html
   <!DOCTYPE html>
   <html>
   <head>
       <title>{% block title %}My Website{% endblock %}</title>
   </head>
   <body>
       <header>
           <h1>Welcome to My Website</h1>
       </header>
       <main>
           {% block content %}{% endblock %}
       </main>
       <footer>
           <p>Footer Content</p>
       </footer>
   </body>
   </html>
   ```

2. **Extend the Base Template** (e.g., `home.html`):
   ```html
   {% extends 'base.html' %}

   {% block title %}Home Page{% endblock %}

   {% block content %}
   <p>This is the home page content.</p>
   {% endblock %}
   ```

### Benefits of Template Inheritance
- Reduces code duplication
- Ensures consistent design across pages
- Makes maintenance easier

---

## URL Tags in Django
Django’s `{% url %}` template tag allows you to dynamically generate URLs in templates instead of hardcoding them.

### Basic Usage
```html
<a href="{% url 'home' %}">Home</a>
```
Here, `'home'` refers to a **named URL pattern** in `urls.py`:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

### URL with Parameters
If a URL takes parameters, pass them inside the `{% url %}` tag:
```html
<a href="{% url 'profile' user.id %}">View Profile</a>
```
Corresponding URL pattern:
```python
path('profile/<int:id>/', views.profile, name='profile')
```

### Benefits of Using `{% url %}`
- Avoids hardcoding URLs, making changes easier
- Ensures URLs remain consistent across the project
- Works well with named routes and dynamic paths

---

## Conclusion
Django’s **template inheritance** and **URL tags** are essential tools for building scalable, maintainable web applications. They help you structure your templates efficiently and keep your URLs dynamic and manageable.

Happy coding! 🚀

