
from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech

# YOUR PROJECT ID
PROJECT_ID = "project-f1618e93-f388-4e5e-bee"

# YOUR LOCATION
LOCATION = "us-east1"

client = SpeechClient(
    client_options={"api_endpoint": f"{LOCATION}-speech.googleapis.com"}
)

# Add your audio file here! Test with Sandshrew.wav if you want. Keep your audio short (<30s)
with open("resources/Tapping.wav", "rb") as f:
    audio_content = f.read()

config = cloud_speech.RecognitionConfig(
    auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
    language_codes=["en-US"],
    model="short",
)

request = cloud_speech.RecognizeRequest(
    recognizer=f"projects/{PROJECT_ID}/locations/{LOCATION}/recognizers/_",
    config=config,
    content=audio_content,
)

# Transcribes the audio into text
response = client.recognize(request=request)

for result in response.results:
    print(f"Transcript: {result.alternatives[0].transcript}")
    print(f"Confidence: {result.alternatives[0].confidence:.2f}")

