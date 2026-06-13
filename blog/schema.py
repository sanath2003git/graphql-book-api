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

    search_book = graphene.List(
    BookType,
    word=graphene.String(required=True)
)

    def resolve_books(self, info):
        return Book.objects.all()
    
    def resolve_book(self, info, id):
        try:
            return Book.objects.get(id=id)

        except Book.DoesNotExist:
            return None
        
    def resolve_search_book(self, info, word):

        return Book.objects.filter(
        title__icontains=word
        )


schema = graphene.Schema(query=Query)