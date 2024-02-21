import graphene
from sweetener.resolvers import QueryResolver
"""
Sample Query:

query {
  circleArea: getCircle(radius: 5)
  rectangleArea: getRectangle(width: 10, height: 20)
  triangleArea: getTriangle(base: 5, height: 10)
  squareArea: getSquare(side: 4)
  TrapezoidArea: getTrapezoid(base1: 2, base2: 4, height: 10)
}

Sample Output:

{
  "data": {
    "circleArea": 78.5,
    "rectangleArea": 200,
    "triangleArea": 25,
    "squareArea": 16,
    "TrapezoidArea": 30
  }
}
"""


class Query(graphene.ObjectType):
    getCircle = graphene.Float(radius=graphene.Float())
    getRectangle = graphene.Float(
        width=graphene.Float(), height=graphene.Float())
    getTriangle = graphene.Float(
        base=graphene.Float(), height=graphene.Float())
    getSquare = graphene.Float(
        side=graphene.Float()
    )
    getTrapezoid = graphene.Float(
        base1=graphene.Float(),
        base2=graphene.Float(),
        height=graphene.Float()
    )

    def resolve_getCircle(self, info, radius):
        return QueryResolver.getCircle(radius)

    def resolve_getRectangle(self, info, width, height):
        return QueryResolver.getRectangle(width, height)

    def resolve_getTriangle(self, info, base, height):
        return QueryResolver.getTriangle(base, height)

    def resolve_getSquare(self, info, side):
        return QueryResolver.getSquare(side)

    def resolve_getTrapezoid(self, info, base1, base2, height):
        return QueryResolver.getTrapezoid(base1, base2, height)

    # TODO
    # More shapes would be included


schema = graphene.Schema(query=Query)
