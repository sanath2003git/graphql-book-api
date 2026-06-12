import graphene
from graphene_django import DjangoObjectType

from .models import Book


class BookType(DjangoObjectType):

    class Meta:
        model = Book