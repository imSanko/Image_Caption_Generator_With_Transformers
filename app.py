from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch
from PIL import Image
import streamlit as st

model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
image_processor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

max_length = 16
num_beams = 4
gen_kwargs = {"max_length": max_length, "num_beams": num_beams}

def predict_step(image):
    if image is None:
        return []
    # images = []
    # for image_path in image_paths:
    #     i_image = Image.open(image_path)
    #     if i_image.mode != "RGB":
    #         i_image = i_image.convert(mode="RGB")

    #     images.append(i_image)

    pixel_values = image_processor(images=[image], return_tensors="pt").pixel_values
    pixel_values = pixel_values.to(device)

    output_ids = model.generate(pixel_values, **gen_kwargs)

    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    preds = [pred.strip() for pred in preds]
    return preds

def main():
    st.title("Image Caption Generator")

    # Upload an image
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Generate captions
        captions = predict_step(image)

        if captions:
            st.subheader("Generated Captions")
            for caption in captions:
                st.write(f"- {caption}")
        else:
            st.write("No captions generated.")

if __name__ == "__main__":
    main()