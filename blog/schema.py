import graphene
from graphene_django import DjangoObjectType

from .models import Book


class BookType(DjangoObjectType):

    class Meta:
        model = Book


class Query(graphene.ObjectType):

    books = graphene.List(BookType)

    book = graphene.Field(
        BookType,
        id=graphene.Int(required=True)
    )

    def resolve_books(self, info):
        return Book.objects.all()
    
    def resolve_book(self, info, id):
        try:
            return Book.objects.get(id=id)

        except Book.DoesNotExist:
            return None


schema = graphene.Schema(query=Query)