import replicate 
import os
import gradio as gr
os.environ["REPLICATE_API_TOKEN"] = ""


def display(prompt):
    output = replicate.run(
    "deforum/deforum_stable_diffusion:e22e77495f2fb83c34d5fae2ad8ab63c0a87b6b573b6208e1535b23b89ea66d6",
    input={
        "fps": 15,
        "zoom": "0: (1.04)",
        "angle": "0:(0)",
        "sampler": "klms",
        "max_frames": 100,
        "translation_x": "0: (0)",
        "translation_y": "0: (0)",
        "color_coherence": "Match Frame 0 LAB",
        "animation_prompts": prompt
    }
)
    return output



video_demo = gr.Interface(
    theme=gr.themes.Soft(),
    fn=display,
    inputs=[gr.components.Textbox(label='Input text')],
    outputs=gr.components.Video(label='Generated Video'),
    allow_flagging='never'
)
