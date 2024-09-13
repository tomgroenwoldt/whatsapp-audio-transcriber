from fastapi import FastAPI, File, UploadFile
from faster_whisper import WhisperModel
import os

# Initialize the model once when the application starts
model_size = "tiny"
model = WhisperModel(model_size, device="cpu", compute_type="int8")

app = FastAPI()


@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    # Save the uploaded audio file to a temporary location
    file_location = f"temp_{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())

    # Transcribe the audio file
    segments, info = model.transcribe(file_location, beam_size=5)

    # Delete the temporary file after transcription
    os.remove(file_location)

    # Concatenate all the text segments into one string
    transcription = " ".join([segment.text for segment in segments])

    return transcription


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
