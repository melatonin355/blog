# Django 

Django is a high-level, open-source Python web framework that enables rapid development of secure and maintainable web applications. It follows the Model-View-Template (MVT) architectural pattern, allowing developers to separate an application's data, user interface, and logic. Django's core philosophy revolves around the "batteries-included" approach, providing a wide array of built-in features and tools to streamline web development.

Created in 2005, Django has since become a popular choice among developers and businesses for its scalability, flexibility, and ease of use. Its robust ecosystem includes a large community of developers, extensive documentation, and a plethora of third-party packages, making it an attractive choice for Software Engineers who require a comprehensive solution for building complex web applications.




Django System Design (MVT pattern):

```
  +---------+     +-------+     +---------+
  |  Model  |<--->| View  |<--->| Template |
  +---------+     +-------+     +---------+
       |              |              |
       |              |              |
  +---------+     +-------+     +---------+
  |  Database  |     |  Logic  |     |  User Interface  |
  +---------+     +-------+     +---------+
```

Typical Django 4 Project Folder Structure:

```
project_name/
|-- project_name/
|   |-- __init__.py
|   |-- asgi.py
|   |-- settings.py
|   |-- urls.py
|   |-- wsgi.py
|-- app_name/
|   |-- migrations/
|   |   |-- __init__.py
|   |-- static/
|   |   |-- app_name/
|   |       |-- css/
|   |       |-- js/
|   |       |-- img/
|   |-- templates/
|   |   |-- app_name/
|   |       |-- index.html
|   |-- __init__.py
|   |-- admin.py
|   |-- apps.py
|   |-- models.py
|   |-- tests.py
|   |-- views.py
|-- manage.py
|-- .gitignore
|-- requirements.txt
```


## Cheatsheet

Django Cheatsheet

1. Installation
```
pip install django
```

2. Create a new Django project
```
django-admin startproject project_name
```

3. Create a new Django app
```
python manage.py startapp app_name
```

4. Run development server
```
python manage.py runserver
```

5. Create a migration
```
python manage.py makemigrations app_name
```

6. Apply migrations
```
python manage.py migrate
```

7. Create a new superuser
```
python manage.py createsuperuser
```

8. Start Django shell
```
python manage.py shell
```

9. Basic Model definition
```python
from django.db import models

class ModelName(models.Model):
    field_name = models.FieldType(options)
```

10. Basic View definition
```python
from django.http import HttpResponse

def view_name(request):
    return HttpResponse("Hello, World!")
```

11. Basic URL configuration
```python
from django.urls import path
from . import views

urlpatterns = [
    path('example/', views.view_name, name='view_name'),
]
```

12. Basic Template usage
```html
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
</head>
<body>
    <h1>{{ heading }}</h1>
    <p>{{ content }}</p>
</body>
</html>
```

13. Include app URLs in the project
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app_name/', include('app_name.urls')),
]
```

14. Serving static files in development
```python
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

15. Importing and using Django models
```python
from app_name.models import ModelName

# Create a new instance
instance = ModelName(field_name=value)

# Save the instance
instance.save()

# Query all instances
instances = ModelName.objects.all()

# Query instances with filter
filtered_instances = ModelName.objects.filter(field_name=value)

# Get a single instance by primary key
instance = ModelName.objects.get(pk=primary_key)
```

This is a basic cheatsheet for Django. For more detailed information and advanced usage, consult the official Django documentation at https://docs.djangoproject.com/.
