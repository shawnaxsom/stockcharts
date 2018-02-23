import graphene
import json
import requests

# class Query(graphene.ObjectType):
class Query(graphene.AbstractType):
    peers = graphene.String(symbol=graphene.String())
    chart = graphene.String(symbol=graphene.String(), timespan=graphene.String())

    def resolve_peers(self, info, symbol):
        return json.loads(requests.get('https://api.iextrading.com/1.0/stock/' + symbol + '/peers').content)

    def resolve_chart(self, info, symbol, timespan):
        return json.loads(requests.get('https://api.iextrading.com/1.0/stock/' + symbol + '/chart/' + timespan).content)

# schema = graphene.Schema(query=Query)

# result = schema.execute('''
#     {
#       chart(symbol: "msft", timespan: "5y")
#       peers(symbol: "msft")
#     }
#     ''')
# print(result.data)

