import gradio as gr
import os
import replicate
from dotenv import load_dotenv
load_dotenv()

<<<<<<< HEAD:backend/music_model.py
os.environ["REPLICATE_API_TOKEN"] = os.getenv('REPLICATE_API_TOKEN')
=======
os.environ["REPLICATE_API_TOKEN"] = ""
>>>>>>> 83b7bf497826fb5e3868070f51372d4cd097b693:Music_AI/music_model.py

def generateMusic(text):
    text = text.replace("\n", " ")
    input = {
        "prompt": text,
        "model_version": "stereo-large",
        "output_format": "mp3",
        "normalization_strategy": "peak"
    }
    output = replicate.run(
        "meta/musicgen:671ac645ce5e552cc63a54a2bbff63fcf798043055d2dac5fc9e36a837eedcfb",
        input=input
    )
    return output

music = gr.Interface(
    fn=generateMusic,
    inputs=gr.Textbox(lines= 2, placeholder="Type Anthing to Generate Music..."),
    outputs="audio",
    title="Music Generator",
)