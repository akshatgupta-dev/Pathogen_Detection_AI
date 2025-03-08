# import torch
# import torch.nn as nn
# import torch.optim as optim

# class ResistancePredictor(nn.Module):
#     def __init__(self, input_size):
#         super(ResistancePredictor, self).__init__()
#         self.fc = nn.Linear(input_size, 2)  # Binary classification (Resistant/Not)

#     def forward(self, x):
#         return self.fc(x)

# # Train on resistance dataset...
# model = ResistancePredictor(input_size=128)  # Example feature size
# torch.save(model.state_dict(), "models/resistance_predictor.pth")


import torch
import torchvision.models as models

# ✅ Define the number of classes
num_bacteria_classes = 5  # Change if needed
num_resistance_classes = 2  # Resistant / Non-resistant

# ✅ Load and modify ResNet18 model for bacterial detection
bacterial_detection_model = models.resnet18(weights=None)
bacterial_detection_model.fc = torch.nn.Linear(bacterial_detection_model.fc.in_features, num_bacteria_classes)

# ✅ Load bacterial detection model weights
bacteria_model_path = "/home/akshatgg/projects/Pathogen_Detection_AI/models/bacteria_detector.pth"
try:
    bacterial_detection_model.load_state_dict(torch.load(bacteria_model_path, map_location="cpu"), strict=False)
    print("✅ Bacterial detection model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading bacterial detection model: {e}")

# ✅ Put bacterial model in evaluation mode
bacterial_detection_model.eval()

# ✅ Load and modify ResNet18 model for antibiotic resistance prediction
antibiotic_resistance_model = models.resnet18(weights=None)
antibiotic_resistance_model.fc = torch.nn.Linear(antibiotic_resistance_model.fc.in_features, num_resistance_classes)

# ✅ Load antibiotic resistance model weights
resistance_model_path = "/home/akshatgg/projects/Pathogen_Detection_AI/models/resistance_predictor.pth"
try:
    antibiotic_resistance_model.load_state_dict(torch.load(resistance_model_path, map_location="cpu"), strict=False)
    print("✅ Antibiotic resistance model loaded successfully!")
except Exception as e:
    print(f"❌ Error loading antibiotic resistance model: {e}")

# ✅ Put resistance model in evaluation mode
antibiotic_resistance_model.eval()
