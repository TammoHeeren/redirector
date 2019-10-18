import json
import datetime
import boto3


def nothing_here_to_see():
    return {'statusCode': 200,
            'body': 'Nothing here to see',
            'headers': {'Content-Type': 'text/html'},
            }


def redirect(target):
    return {
        'statusCode': 303,
        'headers': {'Location': target}
    }


def handler(event, context):

    # if not event is given, just return
    if not event:
        return nothing_here_to_see()

    # get path parameters
    path_parameters = event.get('pathParameters')

    # if no path parameter is given, just return
    if not path_parameters:
        return nothing_here_to_see()

    # get short url
    short = path_parameters.get('short')

    # if short is empty, just return
    if not short:
        return nothing_here_to_see()

    short = short.lower()

    # Get the redirect link from dynamodb
    dynamodb = boto3.resource(
        'dynamodb',
        region_name='us-west-2',
    )

    table = dynamodb.Table('tammo.us')

    response = table.get_item(
        Key={
            'target': short
        }
    )

    item = response.get('Item')

    if not item:
        return nothing_here_to_see()

    target = item.get('link')

    if not target:
        return nothing_here_to_see()

    return redirect(target)