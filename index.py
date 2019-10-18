import json
import datetime


def nothing_here_to_see():
    return {'statusCode': 200,
            'body': 'Nothing here to see',
            'headers': {'Content-Type': 'text/html'},
            }


def redirect_to_here(target):
    body = f'''<!DOCTYPE html>
    <html>
      <head>
        <meta http-equiv="Refresh" content="7; url={target}" />
      </head>
      <body>
        <p>Please follow <a href="{target}">this link</a>.</p>
      </body>
    </html>'''
    return {'statusCode': 200,
            'body': body,
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

    if short.lower() == 'linkedin':
        target = 'https://www.linkedin.com/in/tammoheeren/'
        return redirect(target)

    return nothing_here_to_see()