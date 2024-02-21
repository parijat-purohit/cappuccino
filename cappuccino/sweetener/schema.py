import graphene
from sweetener.resolvers import QueryResolver


class Query(graphene.ObjectType):
    getCircle = graphene.Float(radius=graphene.Float())
    getRectangle = graphene.Float(
        width=graphene.Float(), height=graphene.Float())
    getTriangle = graphene.Float(
        base=graphene.Float(), height=graphene.Float())

    def resolve_getCircle(self, info, radius):
        return QueryResolver.getCircle(radius)

    def resolve_getRectangle(self, info, width, height):
        return QueryResolver.getRectangle(width, height)

    def resolve_getTriangle(self, info, base, height):
        return QueryResolver.getTriangle(base, height)


schema = graphene.Schema(query=Query)
