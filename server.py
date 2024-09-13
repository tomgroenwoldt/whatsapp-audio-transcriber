import os
import requests

from base64 import b64encode
from dotenv import load_dotenv
from fastapi import FastAPI, Form
from faster_whisper import WhisperModel
from twilio.rest import Client

load_dotenv()

app = FastAPI()

# Retrieve environment variables
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")

# Prepare the basic authentication header
auth_str = f"{TWILIO_ACCOUNT_SID}:{TWILIO_AUTH_TOKEN}"
auth_bytes = auth_str.encode("utf-8")
auth_b64 = b64encode(auth_bytes).decode("utf-8")
headers = {"Authorization": "Basic " + auth_b64}

# Initialize Whisper model
model_size = "small"
model = WhisperModel(model_size, device="auto", compute_type="int8")

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)


@app.post("/transcribe/")
async def transcribe_audio(
    To: str = Form(...),
    From: str = Form(...),
    MediaUrl0: str = Form(...),
):
    # Download the media file
    file_response = requests.get(MediaUrl0, headers=headers, stream=True)

    # Save the file for the model.
    file_content = file_response.content
    input_path = "input.ogg"
    with open(input_path, "wb") as f:
        f.write(file_content)

    # Transcribe the audio file via fast-whisper.
    segments, info = model.transcribe(input_path, beam_size=5)
    transcript = " ".join(segment.text for segment in segments)

    # Send the transcription via twilio to the user.
    client.messages.create(to=From, from_=To, body=transcript)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
