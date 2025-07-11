from celery import shared_task
from celery import shared_task
from .models import HandwritingSample
import torch
from torchvision import transforms
from PIL import Image
import os

@shared_task
def analyze_image(image_id):
    instance = HandwritingSample.objects.get(id=image_id)
    image_path = instance.image_file.path

    # Load image
    img = Image.open(image_path).convert("RGB")
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor()
    ])
    tensor = transform(img).unsqueeze(0)  # (1, C, H, W)

    # Load model (mock example)
    model = torch.load('parkinson_cnn.pth', map_location=torch.device('cpu'))
    model.eval()
    with torch.no_grad():
        output = model(tensor)
        prediction = "Parkinson" if output.argmax(1).item() == 1 else "Normal"

    # Save prediction to instance
    instance.prediction = prediction
    instance.save()

@shared_task
def run_prediction(sample_id):
    print("Running prediction for:", sample_id)
    # Load model, predict, store result...
