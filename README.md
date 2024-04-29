---

# Image Caption Generator With Transformers

This repository contains code for generating captions for images using a Transformer-based model. The model used is the `VisionEncoderDecoderModel` from the Hugging Face Transformers library, specifically the `nlpconnect/vit-gpt2-image-captioning` model.

## Installation

To run this code, you'll need to install the following packages:

- [Transformers](https://huggingface.co/transformers/)
- [PyTorch](https://pytorch.org/)
- [Pillow (Python Imaging Library)](https://python-pillow.org/)

Certainly! Here's an updated installation section with more detailed instructions:

---

## Installation

### 1. Clone the Repository

First, clone this repository to your local machine using Git:

```bash
git clone https://github.com/your-username/Image_Caption_Generator_With_Transformers.git
```

Replace `your-username` with your GitHub username.

### 2. Install Required Packages

Navigate to the cloned repository and install the required Python packages using pip:

```bash
cd Image_Caption_Generator_With_Transformers
pip install -r requirements.txt
```

### 3. Download Pre-trained Model and Tokenizer

Download the pre-trained `nlpconnect/vit-gpt2-image-captioning` model and tokenizer from the Hugging Face model hub using the `transformers` library:

```bash
python download_model.py
```

This will download the necessary model files and save them to the `models` directory.

### 4. Verify Installation

To verify that the installation was successful, you can run the provided example usage code:

```bash
python example_usage.py
```

This will generate captions for a sample image (`sample.jpg`) and print the captions to the console.

---

## Usage

1. Import the required libraries and load the pre-trained model and tokenizer:

```python
from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer
import torch
from PIL import Image
```

2. Call the `predict_step` function with a list of image paths to generate captions:

```python
captions = predict_step(['sample2.jpg'])
print(captions)
```

This will output the generated captions for the given image(s).

The provided code includes an example usage:

```python
predict_step(['sample2.jpg'])
```

---

## Deployment

### 1. Prepare Your Streamlit App

Make sure your Streamlit app (`app.py`) is ready for deployment. Ensure that it includes all necessary dependencies and functionality.

### 2. Create a Requirements File

Create a `requirements.txt` file in your project directory listing all the dependencies needed by your Streamlit app. You can generate this file using `pip freeze > requirements.txt` if you're using a virtual environment.

### 3. Set Up a GitHub Repository

If you haven't already, set up a GitHub repository for your Streamlit app. Push your `app.py` and `requirements.txt` files to this repository.

### 4. Deploy on Streamlit Sharing

1. Go to [Streamlit Sharing](https://share.streamlit.io/) and sign in with your GitHub account.
2. Click on "New app" and select your GitHub repository.
3. Configure the settings for your app (e.g., branch, path to `app.py`).
4. Click on "Deploy" to deploy your Streamlit app.

### 5. Monitor Deployment

Streamlit will start building and deploying your app. You can monitor the deployment process in the Streamlit Sharing dashboard.

### 6. View Your App

Once deployed, you can access your Streamlit app using the provided URL. Share this URL with others to showcase your app.

### 7. Update Your App

If you make changes to your app, simply push the changes to your GitHub repository. Streamlit Sharing will automatically redeploy your app with the new changes.

### 8. Manage Your App

You can manage your deployed app in the Streamlit Sharing dashboard. From here, you can view logs, change settings, and monitor usage.

---

### Docker Deployment

```Dockerfile
# Use the official Python image as the base image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port for the Streamlit app (default is 8501)
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "app.py"]
```

Here's what the different parts of the Dockerfile do:

1. `FROM python:3.9`: This line specifies the base image for your Docker container. In this case, we're using the official Python 3.9 image.

2. `WORKDIR /app`: This sets the working directory inside the container to `/app`.

3. `COPY requirements.txt .`: This copies the `requirements.txt` file from your local machine to the container's working directory.

4. `RUN pip install --no-cache-dir -r requirements.txt`: This line installs the Python packages listed in the `requirements.txt` file.

5. `COPY . .`: This copies the entire contents of your local project directory (including the Streamlit app code) to the container's working directory.

6. `EXPOSE 8501`: This exposes port 8501 in the container, which is the default port that Streamlit runs on.

7. `CMD ["streamlit", "run", "app.py"]`: This is the command that will be executed when the container starts. It runs the `streamlit run app.py` command to start the Streamlit app.

To build the Docker image, navigate to the directory containing the Dockerfile and run the following command:

```
docker build -t image-caption-generator .
```

This will build a Docker image with the tag `image-caption-generator`.

To run the container and start the Streamlit app, use the following command:

```
docker run -p 8501:8501 image-caption-generator
```

This command maps the container's port 8501 to the host's port 8501, so you can access the Streamlit app in your web browser at `http://localhost:8501`.

Make sure to replace `app.py` with the name of your Streamlit app file if it's different.

With this Dockerfile, you can easily build and run your Streamlit image caption generator app in a Docker container, ensuring a consistent and isolated environment for your application.

---

