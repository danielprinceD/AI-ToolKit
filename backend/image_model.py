import gradio as gr
from pathlib import Path
import torch
import pandas as pd
import numpy as np
from diffusers import StableDiffusionPipeline
from transformers import pipeline, set_seed
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

class CFG:
    device = "cpu"
    seed = 42
    generator = torch.Generator(device).manual_seed(seed)
    image_gen_steps = 10
    image_gen_model_id = "stabilityai/stable-diffusion-2"
    image_gen_size = (400,400)
    image_gen_guidance_scale = 9
    prompt_gen_model_id = "gpt2"
    prompt_dataset_size = 6
    prompt_max_length = 12
    
    
image_gen_model = StableDiffusionPipeline.from_pretrained(
CFG.image_gen_model_id, torch_dtype=torch.float32,
varient="fp16", use_auth_token='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', guidance_scale=9
)
image_gen_model = image_gen_model.to(CFG.device)


def generateImage(prompt):
    image = image_gen_model(
        prompt, num_inference_steps=CFG.image_gen_steps,
        generator=CFG.generator,
        guidance_scale=CFG.image_gen_guidance_scale
    ).images[0]
    
    image = image.resize(CFG.image_gen_size)
    return image


image = gr.Interface(
    fn=generateImage,
    inputs=gr.Textbox(lines= 2, placeholder="Type Anthing to Generate Image..."),
    outputs="image",
    title="Image Generator",
)