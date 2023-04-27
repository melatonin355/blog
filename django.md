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
