import json
import datetime

TARGETS = {
    'linkedin': 'https://www.linkedin.com/in/tammoheeren/',
    'resume': 'https://docs.google.com/document/d/1o4CFp0deSyMi0qvI74HG3m5IY7uf7-bgYwvKEUpstQw/edit?usp=sharing',
    'resume-orthalign': 'https://docs.google.com/document/d/1o8iaNSlimF1z0VQx5aAxsKxUXts0oBWvXd8fJV8rNfs/edit?usp=sharing',
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