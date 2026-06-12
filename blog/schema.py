import graphene
from graphene_django import DjangoObjectType

from .models import Book


class BookType(DjangoObjectType):

    class Meta:
        model = Book


class Query(graphene.ObjectType):

    books = graphene.List(BookType)

    def resolve_books(self, info):
        return Book.objects.all()


schema = graphene.Schema(query=Query)