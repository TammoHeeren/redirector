import boto3


# Name of the able that stores the redirect information
# Minimum fields are:
# target: the stuff after you domain name
# link: where the redirect is pointing towards
#
# Example:
# https://tammo.us/example -> https://www.example.com
# then
# target = 'example'
# link = 'https://www.example.com'

table_name = 'tammo.us'
region_name = 'us-west-2'


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
        region_name=region_name,
    )

    table = dynamodb.Table(table_name)

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