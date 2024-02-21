import graphene


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
