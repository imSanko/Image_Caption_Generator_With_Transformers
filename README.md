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

model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
feature_extractor = ViTFeatureExtractor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

Define the parameters for the caption generation:

pythonCopy codemax_length = 16
num_beams = 4
gen_kwargs = {"max_length": max_length, "num_beams": num_beams}

Define a function to generate captions for a list of image paths:

pythonCopy codedef predict_step(image_paths):
    images = []
    for image_path in image_paths:
        i_image = Image.open(image_path)
        if i_image.mode != "RGB":
            i_image = i_image.convert(mode="RGB")

        images.append(i_image)

    pixel_values = feature_extractor(images=images, return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)

    output_ids = model.generate(pixel_values, **gen_kwargs)

    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    preds = [pred.strip() for pred in preds]
    return preds

Call the predict_step function with a list of image paths to generate captions:

pythonCopy codecaptions = predict_step(['sample2.jpg'])
print(captions)
This will output the generated captions for the given image(s).
## Example
The provided code includes an example usage:
pythonCopy codepredict_step(['sample2.jpg'])
