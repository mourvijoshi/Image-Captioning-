import gradio as gr
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import requests
from io import BytesIO

# Load BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Function to generate image caption
def generate_caption(image):
    inputs = processor(images=image, return_tensors="pt")
    outputs = model.generate(**inputs)
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    return caption

# Extra Feature: Function to fetch image from a URL
def caption_from_url(url):
    try:
        response = requests.get(url)
        img = Image.open(BytesIO(response.content))
        caption = generate_caption(img)
        return caption
    except Exception as e:
        return f"Error: {str(e)}"

# Main interface with enhanced design and features
def caption_image(image):
    try:
        caption = generate_caption(image)
        return caption
    except Exception as e:
        return f"Error: {str(e)}"

# Setting up the Gradio interface
with gr.Blocks(theme="default") as iface:

    # Title and description
    gr.Markdown(
        """
        # Image Captioning with BLIP
        **Upload an image or provide an image URL to generate a caption.**
        """
    )

    # Tabs for functionality
    with gr.Tab("Upload Image"):
        # Upload an image and generate caption
        image_input = gr.Image(type="pil", label="Upload an image")
        output = gr.Textbox(label="Generated Caption")
        submit_btn = gr.Button("Generate Caption")
        submit_btn.click(caption_image, inputs=image_input, outputs=output)

    with gr.Tab("Image from URL"):
        # Generate caption from URL
        url_input = gr.Textbox(label="Enter image URL")
        url_output = gr.Textbox(label="Generated Caption")
        url_submit_btn = gr.Button("Generate from URL")
        url_submit_btn.click(caption_from_url, inputs=url_input, outputs=url_output)

    # Layout and styling improvements
    gr.Markdown("""
    ## Customize Image Captioning
    ### Upload your image or provide a URL, and we'll do the rest!
    """)
    
    with gr.Row():
        gr.Image(type="pil", label="Optional Resize (in pixels)")
        gr.Slider(50, 512, label="Width")
        gr.Slider(50, 512, label="Height")

# Launch the interface
iface.launch()
