# WhatsApp Audio Transcription with Twilio and Whisper Model

![image](https://github.com/user-attachments/assets/0c291ac1-bfb0-45ed-937d-af23df6759a7)

This project is a FastAPI-based web service that transcribes a users WhatsApp
audio files using the Whisper model and sends the transcriptions via Twilio back
to the user.

## Features

- Accepts audio files sent via mobile WhatsApp clients through Twilio webhook.
- Transcribes audio using [Faster Whisper](https://github.com/SYSTRAN/faster-whisper).
- Sends transcriptions back to the sender's phone number via Twilio.

## Setup Application

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repository.git
cd your-repository
```

### 2. Install requirements

```bash
python -m venv .venv
.venv/bin/pip install -r requirements.txt
```

### 3. Run the project

```bash
.venv/bin/python server.py
```
**If you want this to work with Twilio you have to expose this service to some
public IP. Otherwise, Twilio is unable to reach this service.**

## Setup Twilio Sandbox

Follow [the guide](https://www.twilio.com/docs/whatsapp/sandbox) in your
favorite programming language to setup the WhatsApp sandbox. The main steps are:

- Create a WhatsApp sandbox.
- Join the sandbox with a phone.
- Set the webhook URL.
