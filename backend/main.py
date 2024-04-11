from fastapi import FastAPI
import gradio as gr
from chat_app import chat_demo
from video_app import video_demo
from image_model import image
from code_model import code
from music_model import music
app = FastAPI()

@app.get('/')
async def root():
    return {"status" : 200}

app1 = gr.mount_gradio_app(app, chat_demo, path='/chat')
app2 = gr.mount_gradio_app(app, video_demo, path='/video')
app3 = gr.mount_gradio_app(app, image, path='/image')
app4 = gr.mount_gradio_app(app, code, path='/code_gen')
app5 = gr.mount_gradio_app(app, music, path='/audio')