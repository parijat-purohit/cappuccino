from django.urls import include, re_path
from graphene_django.views import GraphQLView
from sweetener.schema import schema

urlpatterns = [
    re_path('graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]
