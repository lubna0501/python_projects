from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
from io import BytesIO

class BlipCaptioning:
    def __init__(self):
        self.model_name = 'Salesforce/blip-image-captioning-base'
        self.processor = BlipProcessor.from_pretrained(self.model_name)
        self.model = BlipForConditionalGeneration.from_pretrained(self.model_name)

    def generate_caption(self, image_path):
        with open(image_path, "rb") as f:
            image_bytes = f.read()

        inputs = self.processor(images=Image.open(BytesIO(image_bytes)), return_tensors="pt")
        outputs = self.model.generate(**inputs)
        caption = self.processor.decode(outputs[0], skip_special_tokens=True)
        return caption

# Example usage
blip_captioner = BlipCaptioning()
caption = blip_captioner.generate_caption("lubna.jpg")
print("BLIP Caption:", caption)
