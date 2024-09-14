# WhatsApp Audio Transcription with Twilio and Whisper Model

This project is a FastAPI-based web service that transcribes a users WhatsApp
audio files using the Whisper model and sends the transcriptions via Twilio back
to the user.

https://github.com/user-attachments/assets/4916d08d-0511-445a-833f-af93c0ea896b

## Features

- Accepts audio files sent via mobile WhatsApp clients through Twilio webhook.
- Transcribes audio using [Faster Whisper](https://github.com/SYSTRAN/faster-whisper).
- Sends transcriptions back to the sender's phone number via Twilio.

## Setup Twilio Sandbox

Follow [the guide](https://www.twilio.com/docs/whatsapp/sandbox) in your
favorite programming language to setup the WhatsApp sandbox. The main steps are:

- Create a WhatsApp sandbox.
- Join the sandbox with a phone.
- Set the webhook URL.

## Setup Application

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### 2. Install Requirements

```bash
python -m venv .venv
.venv/bin/pip install -r requirements.txt
```

### 3. Add Your Twilio Credentials

```bash
cp .env.example .env
```

Open `.env` with your favorite editor and add your Twilio credentials:

```bash
TWILIO_ACCOUNT_SID = "your_account_sid_here"
TWILIO_AUTH_TOKEN = "your_auth_token_here"
```

### 4. Run the Project

```bash
.venv/bin/python server.py
```
**If you want this to work with Twilio you have to expose this service to some
public IP. Otherwise, Twilio is unable to reach this service.**

#### 4.1 Use Container Image

This repository provides a container image. Pull it with:

```bash
docker pull ghcr.io/tomgroenwoldt/whatsapp-audio-transcriber:main
```

You can run the container by passing your credentials via environment variables:

```bash
docker run -p 8000:8000 -e TWILIO_ACCOUNT_SID="your_account_sid_here" -e TWILIO_AUTH_TOKEN="your_auth_token_here" ghcr.io/tomgroenwoldt/whatsapp-audio-transcriber:main
```

Alternatively, you can setup a `compose.yml` file that could look something like this:

```yaml
version: "3.3"

services:
  transcriber:
    image: ghcr.io/tomgroenwoldt/whatsapp-audio-transcriber:main
    ports:
      - 8000:8000
    environment:
      - TWILIO_ACCOUNT_SID=your_account_sid_here # Without quotes!
      - TWILIO_AUTH_TOKEN=your_auth_token_here # Without quotes!
```
