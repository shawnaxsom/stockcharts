import json
import logging
import random

log = logging.getLogger()
log.setLevel(logging.DEBUG)

# this adds the component-level `lib` directory to the Python import path
import sys, os
# get this file's directory independent of where it's run from
here = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(here, "./vendored"))

import graphene
import requests

class Query(graphene.ObjectType):
    peers = graphene.String(symbol=graphene.String())
    chart = graphene.String(symbol=graphene.String(), timespan=graphene.String())

    def resolve_peers(self, info, symbol):
        return json.loads(requests.get('https://api.iextrading.com/1.0/stock/' + symbol + '/peers').content)

    def resolve_chart(self, info, symbol, timespan):
        return json.loads(requests.get('https://api.iextrading.com/1.0/stock/' + symbol + '/chart/' + timespan).content)

def handler(event, context):
    schema = graphene.Schema(query=Query)

    print(event)

    query = '''
    {
        peers(symbol: "msft")
    }'''

    result = schema.execute(query)

    response = {
        "statusCode": 200,
        # "body": json.dumps(result.data['peers'])
        "body": json.dumps(event)
    }

    return response


if __name__ == "__main__":
    schema = graphene.Schema(query=Query)

    query = '''
    {
        peers(symbol: "msft")
    }'''

    result = schema.execute(query)

    print(json.dumps(result.data['peers']))
