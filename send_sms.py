# /usr/bin/env python
# -*- coding: utf-8 -*-
"""Show how to send an SMS with Python and Twilio"""

import os

from dotenv import load_dotenv
from twilio.rest import Client

load_dotenv()

# You can find the first three of these values at
# https://twilio.com/user/account
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
sender = os.environ['TWILIO_PHONE_NUMBER']
recipient = os.environ['RECIPIENT']

client = Client(account_sid, auth_token)
client.api.account.messages.create(
    to=recipient,
    from_=sender,
    body="This is the ship that made the Kessel Run in fourteen parsecs?"
)
