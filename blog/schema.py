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

class CreateBook(graphene.Mutation):

    success = graphene.Boolean(required=True)

    book = graphene.Field(BookType)


    class Arguments:

        title = graphene.String(required=True)

        author = graphene.String(required=True)

        price = graphene.Int(required=True)


    def mutate(

        self,

        info,

        title,

        author,

        price

    ):

        book_obj = Book(

            title=title,

            author=author,

            price=price

        )

        book_obj.save()

        return CreateBook(

            success=True,

            book=book_obj

        )
    
class UpdateBook(graphene.Mutation):

    success = graphene.Boolean(required=True)

    book = graphene.Field(BookType)


    class Arguments:

        id = graphene.Int(required=True)

        title = graphene.String()

        author = graphene.String()

        price = graphene.Int()


    def mutate(

        self,

        info,

        id,

        title=None,

        author=None,

        price=None

    ):

        try:

            book_obj = Book.objects.get(id=id)


            if title is not None:

                book_obj.title = title


            if author is not None:

                book_obj.author = author


            if price is not None:

                book_obj.price = price


            book_obj.save()


            return UpdateBook(

                success=True,

                book=book_obj

            )


        except Book.DoesNotExist:

            return UpdateBook(

                success=False,

                book=None

            )
        
class DeleteBook(graphene.Mutation):

    success = graphene.Boolean(required=True)


    class Arguments:

        id = graphene.Int(required=True)


    def mutate(

        self,

        info,

        id

    ):

        try:

            book_obj = Book.objects.get(id=id)

            book_obj.delete()


            return DeleteBook(

                success=True

            )


        except Book.DoesNotExist:


            return DeleteBook(

                success=False

            )
    
class Mutation(graphene.ObjectType):

    create_book = CreateBook.Field()

    update_book = UpdateBook.Field()

    delete_book = DeleteBook.Field()

schema = graphene.Schema(

    query=Query,

    mutation=Mutation

)
