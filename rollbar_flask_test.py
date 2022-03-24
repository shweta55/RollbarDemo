from flask import Flask
app = Flask(__name__)

## Rollbar init code. You'll need the following to use Rollbar with Flask.
## This requires the 'blinker' package to be installed

import os
import rollbar
import rollbar.contrib.flask
from flask import got_request_exception


@app.before_first_request
def init_rollbar():
    """init rollbar module"""
    rollbar.init(
        # access token
        '42c52e40db79498c8ca8694fef842d2f',
        # environment name
        'production',
        # server root directory, makes tracebacks prettier
        root=os.path.dirname(os.path.realpath(__file__)),
        # flask already sets up logging
        allow_logging_basic_config=False)

    rollbar.events.add_payload_handler(payload_handler)
    # send exceptions from `app` to rollbar, using flask's signal system.
    got_request_exception.connect(rollbar.contrib.flask.report_exception, app)


def payload_handler(payload):  # kw is currently unused
    if payload.get('data').get('request').get('headers').get('Sec-Ch-Ua-Platform'):
        payload['data']['request']['headers']['Sec-Ch-Ua-Platform'] = '****'
    return payload

## Simple flask app

@app.route('/')
def hello():
    print("in hello")
    x = None
    x[5]
    return "Hello World!"


if __name__ == '__main__':
    app.run(debug=True)