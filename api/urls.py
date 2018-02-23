from django.urls import path
from graphene_django.views import GraphQLView
from api.schema import schema

urlpatterns = [
    path('graphql', GraphQLView.as_view(graphiql=True, schema=schema)),
]
