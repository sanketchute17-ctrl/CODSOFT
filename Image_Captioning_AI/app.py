import gradio as gr
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image):

    raw_image = Image.fromarray(image).convert("RGB")

    inputs = processor(raw_image, return_tensors="pt")

    output = model.generate(**inputs)

    caption = processor.decode(output[0], skip_special_tokens=True)

    return caption


interface = gr.Interface(
    fn=generate_caption,
    inputs=gr.Image(type="numpy", label="Upload Image"),
    outputs="text",
    title="AI Image Caption Generator",
    description="Upload an image and AI will generate caption."
)

interface.launch(inbrowser=True)