import json
import datetime


def handler(event, context):
    return {'statusCode': 301,
            'headers': {
                'Location': 'https://www.linkedin.com/in/tammoheeren/'
            }
        }
