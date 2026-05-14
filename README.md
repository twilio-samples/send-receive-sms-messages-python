<!-- markdownlint-disable MD013 -->

# Send & receive SMS messages with Python

Learn how to send and receive SMS with Twilio and Python with this repository.
With a minimal amount of code, you can see your phone light up sending and receiving SMS with Twilio and Python.

## Prerequisites

To run the app locally, you need the following:

- [Python][python]
- [ngrok][ngrok] and a free ngrok account
- A [Twilio account][twilio_signup] with an active phone number that can send SMS
- Some command-line/terminal experience would be helpful, but it's not necessary

## Quick Start

First things first, clone or download this repository.
In the repository, you'll see two files: _send_sms.py_ and _receive_sms.py_.
_send_sms.py_ contains just enough code to send an SMS to a recipient from your Twilio phone number.
_receive_sms.py_ contains a small, [Flask][flask] web application that can reply to an SMS received by your Twilio phone number.

### Send an SMS

Before you can send an SMS, you need to complete the following

1. Create a Python virtual environment (if required), and install the [Twilio][twilio_package], Flask, and [python-dotenv][python_dotenv_package] packages

   ```bash
   python -m venv $(pwd)/venv
   source $(pwd)/venv/bin/activate
   python -m pip install python-dotenv
   pip install Flask python-dotenv twilio
   ```

1. Rename the `.env.example` file to `.env`
1. Go to the [Twilio Console][twilio_console] and find your **Account SID**, **Auth Token**, and Twilio phone number.
1. Copy and paste those values into the placeholders in the `.env` file `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, and `TWILIO_PHONE_NUMBER`, respectively.
1. Set your phone number, in [E.164 format][e164_format] as the value of `RECIPIENT` in _.env_
   Save the file.

Then, run the following command to send an SMS.

```bash
python send_sms.py
```

### Receive an SMS

Before you can receive an SMS, you need to complete a few further steps.

1. Start your ngrok server:

   ```bash
   ngrok http 8080
   ```

1. Go to the [Active numbers][active_numbers] page in the Twilio Console.
1. Click your Twilio phone number.
1. Go to the **Configure** tab and find the **Messaging Configuration** section.
1. In the **A call comes in** row, select the **Webhook** option.
1. Paste your ngrok **Forwarding** URL in the **URL** field followed by "/receive/".
   For example, if your ngrok console shows Forwarding "<https://1aaa-123-45-678-910.ngrok-free.app>", enter "<https://1aaa-123-45-678-910.ngrok-free.app/receive/>".
   - To receive an SMS **without** responding to it, append "no-response" to the URL
   - To receive an SMS and respond to it, append "with-response" to the URL
1. Click **Save configuration**.
1. Start the Flask app

   ```bash
   flask --app receive_sms.py --debug run
   ```

1. With both the Flask app and ngrok running, send an SMS to your Twilio phone number, containing whatever message you like.
   If you want a response, try sending "never gonna" as the message.

## Testing

While the code does not have any tests, yet, you can use the [Pylint][pylint] to perform static analysis on the code base.
Then, from the project's top-level directory, install Pylint with the following command:

```bash
python -m pip install pylint
```

Then, run Pylint on the Python source files with the following command:

```bash
pylint *.py
```

Additionally, if you want to validate the documentation (_README.md_) use [MarkdownLint][markdownlint].
To do that, first install it by running the following command:

```bash
npm install markdownlint --save-dev
```

Then, run the following command to validate the documentation with MarkdownLint:

```bash
markdownlint-cli2 README.md
```

[active_numbers]: https://console.twilio.com/us1/develop/phone-numbers/manage/incoming
[e164_format]: https://www.twilio.com/docs/glossary/what-e164
[flask]: https://flask.palletsprojects.com/en/stable/quickstart/
[markdownlint]: https://github.com/davidanson/markdownlint
[ngrok]: https://ngrok.com/
[pylint]: https://pypi.org/project/pylint/
[python]: https://www.python.org/downloads/
[python_dotenv_package]: https://saurabh-kumar.com/python-dotenv/
[twilio_console]: https://console.twilio.com
[twilio_package]: https://github.com/twilio/twilio-python/
[twilio_signup]: https://www.twilio.com/try-twilio

<!-- markdownlint-enable MD013 -->
