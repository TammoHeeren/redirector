import json
import datetime

TARGETS = {
    'linkedin': 'https://www.linkedin.com/in/tammoheeren/',
}


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

    if short.lower() in TARGETS:
        target = TARGETS[short.lower()]
        return redirect(target)

    return nothing_here_to_see()