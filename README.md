
# Image Captioning with BLIP and Gradio

This project is an image captioning tool built using [BLIP (Bootstrapping Language-Image Pretraining)](https://huggingface.co/docs/transformers/model_doc/blip) and [Gradio](https://gradio.app/). The tool generates captions for images uploaded directly or via URL. It's containerized with Docker for easy deployment and requires only minimal setup to get started.

## Features
- **Image Upload:** Upload an image directly from your device to generate a caption.
- **URL Input:** Provide a URL link to an image and receive a caption.
- **User-Friendly Interface:** Developed with Gradio, allowing simple, interactive use.
- **Dockerized:** Easily deployable with Docker, encapsulating dependencies and configurations.

## Project Structure
- **demo.py:** Main application file with Gradio setup and image captioning functions.
- **Dockerfile:** Defines the Docker container for running the application.
- **requirements.txt:** Specifies dependencies.
- **env:** Contains the environment setup files.

## Requirements
To run this project, you'll need:
- Python 3.9
- The packages listed in `requirements.txt`

Alternatively, you can use Docker to avoid manual dependency installation.

## Installation and Setup

### 1. Clone the Repository
bash
git clone https://github.com/yourusername/image-captioning-project.git
cd image-captioning-project

### 2. Run Locally

#### Option 1: Run with Python
1. **Install Dependencies:**
   bash
   pip install -r requirements.txt
   
2. **Run the Application:**
   ```bash
   python demo.py
   ```
   The Gradio app should launch on `http://127.0.0.1:7860`.

#### Option 2: Run with Docker
1. **Build the Docker Image:**
   bash
   docker build -t image-captioning-app .
   
2. **Run the Docker Container:**
   bash
   docker run -p 7860:7860 image-captioning-app
   
   Access the application at `http://localhost:7860`.

## Usage

1. **Upload an Image** or enter an **Image URL**.
2. Click **Generate Caption** to receive a caption for the uploaded image.
   
## Example
Here’s a quick example of how to use the application:

1. Upload an image or enter a URL.
2. Click "Generate Caption."
3. View the generated caption in the output textbox.

## Files Explained

- **`demo.py`:** Contains the main application logic, setting up Gradio's user interface for caption generation.
- **`Dockerfile`:** Builds a Docker image with Python, installs dependencies, and runs the Gradio app.
- **`requirements.txt`:** Lists all required Python packages.
- **`env` folder:** Environment-specific files (if needed).

## License
This project is licensed under the MIT License.
