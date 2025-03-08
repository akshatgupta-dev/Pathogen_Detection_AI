import torch
import torchvision.models as models

# Load a pre-trained model
model = models.resnet18(pretrained=True)
num_features = model.fc.in_features
model.fc = torch.nn.Linear(num_features, 5)  # Assume 5 bacteria classes

# Train on blood smear dataset...
torch.save(model.state_dict(), "models/bacteria_detector.pth")
