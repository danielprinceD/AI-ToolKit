import os
import replicate
import gradio as gr
from dotenv import load_dotenv
from g4f.client import Client



pre_prompt = "You are a helpful assistant. You do not respond as 'User' or pretend to be 'User'. You only respond once as 'Assistant'."


def response(text):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": text+" give me in simple text don't use mark down"}],
    )
    return response.choices[0].message.content
     

with gr.Blocks(theme=gr.themes.Soft()) as chat_demo:
    chatbot = gr.Chatbot()
    msg = gr.Textbox()
    clear = gr.ClearButton([msg, chatbot])

    def respond(message, chat_history):
        bot_message = response(message)
        chat_history.append((message, bot_message))
        return "", chat_history

    msg.submit(respond, [msg, chatbot], [msg, chatbot])