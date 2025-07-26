# TODO: import your module
import os
import send_to_openai as gpt

import requests

# Get the folder where the script is located, done for you
script_dir = os.path.dirname(os.path.abspath(__file__))
frontend = os.path.join(script_dir, "../frontend/src/")
filename = os.path.join(frontend, "downloaded_image.jpg")

IP = "192.168.50.85"

# http://192.168.50.85

url = f"http://{IP}/1024x768.jpg"  # You will have to change the IP Address


# Function to download the image from esp32, given to you
def download_image():
    print("url", url)
    response = requests.get(url)

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Image saved to: {filename}")
    else:
        print("Failed to download image. Status code:", response.status_code)

download_image()

text = gpt.ask_gpt_for_description(filename)
gpt.write_text(text, os.path.join(frontend, "text.txt"))

gpt.request_audio(text, os.path.join(frontend, "tts.wav"))
# gpt.write_audio(audio, os.path.join(frontend, "tts.wav"))

# TODO: Download the image and get a response from openai
