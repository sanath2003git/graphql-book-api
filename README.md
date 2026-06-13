# GraphQL Book API

### Django

- Python web framework
- Used for backend development

### Virtual Environment

- Isolates project dependencies

### Commands

Create environment:
python -m venv venv

Activate:
venv\Scripts\activate

Install Django:
pip install django

Create project:
django-admin startproject core .

Run server:
python manage.py runserver

### Django App

A Django app is a module that handles a specific functionality.

Examples:
- users
- products
- orders
- blog

Create app:

python manage.py startapp blog

Register app:

INSTALLED_APPS = [
    "blog",
]

### Model

A Django Model is a Python class that represents a database table.

### ORM

Object Relational Mapping

Converts Python code into SQL queries.

Example:

Book.objects.all()

### Migrations

makemigrations
- Creates migration files

migrate
- Applies changes to database

### Django Admin

Django provides a built-in admin panel for managing database records.

Register model:

from django.contrib import admin
from .models import Book

admin.site.register(Book)

Create admin user:

python manage.py createsuperuser

Admin URL:

http://127.0.0.1:8000/admin

### Graphene-Django

Graphene-Django connects GraphQL with Django.

Install:

pip install graphene-django

Register:

INSTALLED_APPS = [
    "graphene_django",
]

Configure:

GRAPHENE = {
    "SCHEMA": "blog.schema.schema"
}

### GraphQL Type

A GraphQL Type defines the data structure exposed to GraphQL clients.

### DjangoObjectType

Converts Django models into GraphQL types automatically.

Example:

class BookType(DjangoObjectType):
    class Meta:
        model = Book

### GraphQL Endpoint

URL:

http://127.0.0.1:8000/graphql/

### GraphQLView

Handles GraphQL requests.

### GraphiQL

Browser interface for testing GraphQL queries.

### First Query

{
  books {
    title
    author
    price
  }
}

## Single Book Query

graphene.Field()
returns one object

Arguments:

id=graphene.Int(required=True)

Resolver:

def resolve_book(self, info, id):
    return Book.objects.get(id=id)

Example:

{
  book(id: 1) {
    title
    author
    price
  }
}

## Search Book Query

graphene.String

Used for string arguments.

Example:

word=graphene.String(required=True)

filter()

Used to search objects.

Example:

Book.objects.filter(
    title="Python"
)

Difference

get()
- Returns one object
- Raises exception

filter()
- Returns list
- Returns empty list if not found