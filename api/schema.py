import graphene
import api.stocks.schema

from graphene_django.debug import DjangoDebug


class Query(api.stocks.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass
    # debug = graphene.Field(DjangoDebug, name='__debug')

schema = graphene.Schema(query=Query)
