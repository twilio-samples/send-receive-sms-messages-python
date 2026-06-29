# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

Two standalone Python scripts demonstrating Twilio SMS with Python:

- `send_sms.py` — sends an SMS from a Twilio number to a recipient using the Twilio REST API
- `receive_sms.py` — a Flask app that handles incoming SMS webhooks from Twilio, with two routes: `/receive/no-response` (acknowledges without replying) and `/receive/with-response` (replies with a Rick Astley lyric)

## Setup

```bash
python -m venv $(pwd)/venv
source $(pwd)/venv/bin/activate
pip install Flask python-dotenv twilio
cp .env.example .env
# Fill in TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER, RECIPIENT in .env
```

## Commands

**Send an SMS:**

```bash
python send_sms.py
```

**Run the receive webhook app:**

```bash
flask --app receive_sms.py --debug run
```

The app listens on port 5000 by default.
Expose it via ngrok (`ngrok http 5000`) and configure the ngrok URL as the Twilio webhook.

**Lint Python source:**

```bash
pylint *.py
```

**Lint documentation:**

```bash
markdownlint-cli2 README.md
```

## Environment variables

All credentials are loaded from `.env` via `python-dotenv`.
See `.env.example` for the required variables: `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_PHONE_NUMBER`, `RECIPIENT`.

## Pull requests

Use the template at `.github/PULL_REQUEST_TEMPLATE/pull_request_template.md`.
Commit messages should be concise and written in the imperative mood.
