import json
import datetime


def nothing_here_to_see():
    return {'statusCode': 200,
            'body': 'Nothing here to see',
            'headers': {'Content-Type': 'application/text'},
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

    if short.lower() == 'linkedin':
        return {'statusCode': 301,
                'headers': {
                    'Location': 'https://www.linkedin.com/in/tammoheeren/'
                }
            }

    return nothing_here_to_see()