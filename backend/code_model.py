import gradio as gr
from g4f.client import Client
def generateCode(text):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": text+" give me in simple text don't use mark down"}],
    )
    return response.choices[0].message.content


code = gr.Interface(
    fn=generateCode,
    inputs=gr.Textbox(lines= 2, placeholder="Type your Question Here..."),
    outputs="text",
    title="Code Generator",
)
