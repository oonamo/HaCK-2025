import base64
import os
import secrets

from openai import OpenAI

os.environ["OPENAI_API_KEY"] = secrets.OPENAPI_KEY

client = OpenAI()
PROMPT = """
You are an agent tasked with a secret mission. You must find any important information in the following image
and use it to beat challenges. Respond in 60 words or less. Efficency is important, make sure to keep things understandable, yet brief.
"""


# Image encoding, code provided
def encode_image(image_path):
    with open(image_path, "rb") as image_F:
        return base64.b64encode(image_F.read()).decode("utf-8")


def ask_gpt_for_description(image_path):
    img_bytes = encode_image(image_path)
    response = client.responses.create(
        model="gpt-4.1",
        input=[
            {
                "role": "user",
                "content": [
                    {"type": "input_text", "text": PROMPT},
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{img_bytes}",
                    },
                ],
            }
        ],
    )
    return response.output_text


# TODO: Sending a request and getting a response
# For later: https://platform.openai.com/docs/guides/images-vision?api-mode=responses&format=base64-encoded
def request_image(request: str):
    response = client.responses.create(model="gpt-4.1", input="Say something cool!")
    return response.output_text


def write_text(text, path):
    with open(path, "w") as f:
        f.write(text)


def request_audio(text: str, path):
    with client.audio.speech.with_streaming_response.create(
        model="gpt-4o-mini-tts",
        voice="coral",
        input=text,
    ) as response:
        response.stream_to_file(path)
