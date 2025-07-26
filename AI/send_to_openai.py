import base64
import os
import secrets

from openai import OpenAI

os.environ["OPENAI_API_KEY"] = secrets.OPENAPI_KEY

client = OpenAI()
PROMPT = """
Please show me a cool image!
"""


# Image encoding, code provided
def encode_image(image_path):
    with open(image_path, "rb") as image_F:
        return base64.b64encode(image_F.read()).decode("utf-8")


# TODO: Sending a request and getting a response
# For later: https://platform.openai.com/docs/guides/images-vision?api-mode=responses&format=base64-encoded
def request_image(request: str):
    response = client.responses.create(model="gpt-4.1", input="Say something cool!")
    return response.output_text


# TODO: How do we make things audible?
def request_audio(text: str):
    completion = client.chat.completions.create(
        model="gpt-4o-audio-preview",
        modalities=["text", "audio"],
        audio={"voice": "alloy", "format": "wav"},
        messages=[{"role": "user", "content": text}],
    )
    return completion.choices[0].message


def write_audio(completion):
    wav_bytes = base64.b64decode(completion.audio.data)
    with open("dog.wav", "wb") as f:
        f.write(wav_bytes)


# write_audio(request_audio(request_image("")))

# TODO: Can we put everything together?
