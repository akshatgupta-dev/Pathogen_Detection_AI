from fastapi import FastAPI, File, UploadFile
import torch
import torchvision.models as models
import uvicorn
from PIL import Image
import io
import torchvision.transforms as transforms
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Backend is running!"}

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load and modify ResNet18 model for bacterial detection
bacterial_detection_model = models.resnet18(weights=None)  # Initialize model
num_classes = 5  # Replace with the number of classes in your task
bacterial_detection_model.fc = torch.nn.Linear(bacterial_detection_model.fc.in_features, num_classes)

# Load only the state_dict
state_dict = torch.load(
    "/home/akshatgg/projects/Pathogen_Detection_AI/models/bacteria_detector.pth",
    map_location="cpu"
)

if isinstance(state_dict, dict):  # Ensure it's a state_dict
    bacterial_detection_model.load_state_dict(state_dict)
else:
    raise TypeError("Loaded model is not a valid state_dict!")

bacterial_detection_model.eval()


# # Load and modify ResNet18 model for antibiotic resistance prediction
# antibiotic_resistance_model = models.resnet18(weights=None)
# num_classes = 5  # Replace with the number of classes in your task
# antibiotic_resistance_model.fc = torch.nn.Linear(antibiotic_resistance_model.fc.in_features, num_classes)

# # Load pre-trained model
# antibiotic_resistance_model.load_state_dict(torch.load(
#     "/home/akshatgg/projects/Pathogen_Detection_AI/models/resistance_predictor.pth",
#     map_location="cpu"
# ))
# antibiotic_resistance_model.eval()

# Image preprocessing function
def preprocess_image(image: Image.Image):
    transform = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.5, 0.5, 0.5], std=[0.5, 0.5, 0.5])  # 3-channel normalization
    ])
    return transform(image).unsqueeze(0)  # Add batch dimension


CLASS_NAMES = {
    0: "E. coli",
    1: "Staphylococcus aureus",
    2: "Salmonella",
    3: "Listeria",
    4: "Pseudomonas"
}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    try:
        # Read and preprocess image
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        input_tensor = preprocess_image(image)

        # Run detection model
        with torch.no_grad():
            bacteria_output = bacterial_detection_model(input_tensor)

        # Get prediction class
        bacteria_prediction = torch.argmax(bacteria_output, dim=1).item()
        bacteria_label = CLASS_NAMES.get(bacteria_prediction, "Unknown")

        return {"bacteria_type": bacteria_label}
    
    except Exception as e:
        return {"error": str(e)}



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)