from fastapi import FastAPI
import gradio as gr
from Chat_AI.chat_app import chat_demo
from Video_AI.video_app import video_demo
app = FastAPI()

@app.get('/')
async def root():
    return {"status" : 200}

app1 = gr.mount_gradio_app(app, chat_demo, path='/chat')
app2 = gr.mount_gradio_app(app, video_demo, path='/video')