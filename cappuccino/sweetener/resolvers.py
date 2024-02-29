import graphene
from sweetener.models import Author, Book


class QueryResolver:
    @staticmethod
    def getCircle(radius):
        # Resolver function for calculating the area of a circle
        return 3.14 * radius ** 2

    @staticmethod
    def getRectangle(width, height):
        # Resolver function for calculating the area of a rectangle
        return width * height

    @staticmethod
    def getTriangle(base, height):
        # Resolver function for calculating the area of a triangle
        return 0.5 * base * height

    @staticmethod
    def getSquare(side):
        # Resolver function for calculating the area of a square
        return side * side

    @staticmethod
    def getTrapezoid(base1, base2, height):
        # Resolver function for calculating the area of a trapezoid
        return 0.5 * (base1 + base2) * height

    @staticmethod
    def Authors():
        # Your logic to fetch and potentially filter authors
        return Author.objects.all()

    @staticmethod
    def Books():
        # Your logic to fetch and potentially filter books
        return Book.objects.all()
