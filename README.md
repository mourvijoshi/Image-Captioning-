

# 📸 Image Captioning with BLIP and Gradio

Welcome to the **Image Captioning Tool**! 🚀 Using [BLIP (Bootstrapping Language-Image Pretraining)](https://huggingface.co/docs/transformers/model_doc/blip) and [Gradio](https://gradio.app/), this tool generates captions for images you upload directly or link via URL. It’s also ready to deploy in a Docker container, making setup a breeze! 🎉

---

## 🌟 Key Features
- **🔍 Image Upload:** Generate captions for images you upload directly from your device.
- **🌐 URL Input:** Just provide an image URL, and get a caption in seconds.
- **🖥 User-Friendly Interface:** A simple and interactive Gradio-based UI for seamless interaction.
- **🐳 Dockerized:** Encapsulated in a Docker container for easy deployment and consistent performance.

---

## 🗂 Project Structure
| File                | Description                                                      |
|---------------------|------------------------------------------------------------------|
| **`demo.py`**       | Main application with Gradio setup and image captioning logic    |
| **`Dockerfile`**    | Docker setup for building and running the application            |
| **`requirements.txt`** | Dependencies list for Python packages                        |
| **`env` folder**    | Environment files (optional)                                    |

---

## 🛠️ Requirements

To get started, you'll need:
- **Python 3.9** or higher
- The packages listed in `requirements.txt`

Alternatively, skip the manual setup and run everything with Docker! 🐳

---

## 🚀 Installation and Setup

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/image-captioning-project.git
cd image-captioning-project
```

### Step 2: Run Locally

#### Option 1: Run with Python
1. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Launch the Application:**
   ```bash
   python demo.py
   ```
   **Open in Browser:** [http://127.0.0.1:7860](http://127.0.0.1:7860)

#### Option 2: Run with Docker
1. **Build Docker Image:**
   ```bash
   docker build -t image-captioning-app .
   ```

2. **Run the Docker Container:**
   ```bash
   docker run -p 7860:7860 image-captioning-app
   ```
   **Open in Browser:** [http://localhost:7860](http://localhost:7860)

---

## 🎉 Usage Guide
1. **Upload an Image** or **Enter a URL** of the image you want to caption.
2. Click on **Generate Caption** and let the model work its magic! ✨
3. Your caption appears in the output box, ready to amaze. 📜

---

## 🖼 Example Workflow
1. Upload an image or enter a URL.
2. Click "Generate Caption."
3. Watch as the app crafts a descriptive caption!

---

## 📄 License
This project is available under the MIT License. Feel free to use and modify it as you like!

---

With this setup, you’re ready to dive into the world of AI-driven image captioning!
