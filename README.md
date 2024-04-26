# Image_Caption_Generator_With_Transformers
This repository contains code for generating captions for images using a Transformer-based model. The model used is the `VisionEncoderDecoderModel` from the Hugging Face Transformers library, specifically the `nlpconnect/vit-gpt2-image-captioning` model.
# Image Caption Generator

This repository contains code for generating captions for images using a Transformer-based model. The model used is the `VisionEncoderDecoderModel` from the Hugging Face Transformers library, specifically the `nlpconnect/vit-gpt2-image-captioning` model.

## Installation

To run this code, you'll need to install the following packages:

- Transformers
- PyTorch
- Pillow (Python Imaging Library)

You can install these packages using pip:
pip install transformers torch pillow
Copy code
## Usage

1. Import the required libraries and load the pre-trained model and tokenizer:

```python
from transformers import VisionEncoderDecoderModel, ViTFeatureExtractor, AutoTokenizer
import torch
from PIL import Image


## ** Call the predict_step function with a list of image paths to generate captions:**

pythonCopy codecaptions = predict_step(['sample2.jpg'])
print(captions)
This will output the generated captions for the given image(s).

## **Example**
The provided code includes an example usage:
pythonCopy codepredict_step(['sample2.jpg'])
