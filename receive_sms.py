# -*- coding: utf-8 -*-
"""A small Flask-based app that shows how to respond to messages with Twilio.

Twilio can be configured to reply to incoming messages (SMS, MMS, RCS, and
WhatsApp) with webhooks. These are, effectively, HTTP POST and GET requests.
After Twilio sends one, the application should reply with TwiML, telling Twilio
if it should take subsequent actions or not.

The small Flask-based application in this module shows two different ways of
responding to an incoming SMS via its two routes. One that will send an empty
response, no instructing Twilio to take any further action. One that will
instruct Twilio to send an SMS back to the sender.
"""

import random

from flask import Flask
from flask import request
from twilio.twiml.messaging_response import Message, MessagingResponse

app = Flask(__name__)

@app.post('/receive/no-response')
def no_response():
    """This function handles requests to the "/receive/no-response" route.

    The function's response will contain TwiML that provides no further
    instructions to Twilio. In addition the response's status code will be an
    HTTP 200 OK, and the response will have the Content-Type header set to
    "application/xml; charset=utf-8".
    """
    response = MessagingResponse()

    return str(response)

@app.post('/receive/with-response')
def with_response():
    """This function handles requests to the "/receive/with-response" route.

    If the request's form data contains an element named "Body" with the value
    "never gonna", the function's response will contain TwiML that instructs
    Twilio to send a reply SMS to the sender of the original SMS with a line from
    Rick Astley's hit "Never Gonna Give You Up". Otherwise it sends the same,
    stock line from the same song.

    In addition the response's status code will be an HTTP 200 OK, and the
    response will have the Content-Type header set to "application/xml;
    charset=utf-8".
    """
    response = MessagingResponse()
    message = Message()
    default_option = '''I just wanna tell you how I'm feeling - Gotta make you understand'''

    body = request.form['Body']
    if body.lower() == "never gonna":
        options = (
            'give you up',
            'let you down',
            'make you cry',
            'run around and desert you',
            'say goodbye',
            'tell a lie, and hurt you',
        )
        index = random.randint(1, len(options) - 1)
        message.body(options[index])
    else:
        message.body(default_option)

    response.append(message)

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
