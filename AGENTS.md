# Send & receive SMS messages with Python

Demonstrates how to send and receive SMS messages using the Twilio REST API and Python, with a Flask webhook handler for incoming messages.

## Environment Variables

Copy `.env.example` to `.env`. Never commit `.env`.

```bash
cp .env.example .env
```

| Variable | Where to find | Format |
| -------- | ------------- | ------ |
| `RECIPIENT` | The phone number you want to send SMS to | E.164 format: `+15551234567` |
| `TWILIO_PHONE_NUMBER` | Console → Phone Numbers → Manage → Active Numbers | E.164 format: `+15551234567` |
| `TWILIO_ACCOUNT_SID` | Console homepage or Admin dropdown (top right) → Account Management → Keys & Credentials → API Keys & Tokens | Starts with `AC` |
| `TWILIO_AUTH_TOKEN` | Console homepage or Admin dropdown (top right) → Account Management → Keys & Credentials → API Keys & Tokens → click to reveal | 32-char string. Treat as a password. |

## Commands

```bash
# Install
python -m venv $(pwd)/venv && source $(pwd)/venv/bin/activate && pip install Flask python-dotenv twilio

# Send an SMS
python send_sms.py

# Run the webhook receiver app
flask --app receive_sms.py --debug run

# Expose webhooks locally
# Requires ngrok — install and authenticate at https://ngrok.com before running
ngrok http 5000
# Set the resulting URL + /receive/with-response as the webhook in Twilio Console
```

## Project Structure

- `send_sms.py` — sends a single SMS from your Twilio number to `RECIPIENT`
- `receive_sms.py` — Flask app with two POST routes for handling incoming SMS webhooks
- `.env.example` — template for required credentials

## Agent Boundaries

**Always:**
- Confirm `.env` is configured before running any command
- Use the Environment Variables section to guide the user to each credential — don't ask them to find values without direction
- Confirm the app is running before asking the user to test it

**Never:**
- Run the app with missing or placeholder credentials
- Hardcode credentials or phone numbers in source files
- Skip the `cp .env.example .env` step

## Verify It's Working

**Sending:** Run `python send_sms.py` — the phone number in `RECIPIENT` should receive an SMS within a few seconds.

**Receiving:** Start the Flask app, expose it with ngrok, set the ngrok URL + `/receive/with-response` as the webhook in Twilio Console for your `TWILIO_PHONE_NUMBER`. Text "never gonna" to that number and expect a Rick Astley lyric in reply.

## Twilio Resources

- [Twilio Console](https://console.twilio.com) — credentials, phone numbers, webhook configuration
- [Twilio SMS documentation](https://www.twilio.com/docs/sms)
- [Twilio Python SDK](https://www.twilio.com/docs/libraries/python)
