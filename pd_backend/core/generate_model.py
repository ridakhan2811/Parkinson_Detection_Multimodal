import torch
import torch.nn as nn
import torch.nn.functional as F

class ParkinsonCNN(nn.Module):
    def __init__(self):
        super(ParkinsonCNN, self).__init__()
        self.conv1 = nn.Conv2d(3, 16, kernel_size=3, padding=1)
        self.pool = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(16 * 112 * 112, 2)  # 2 classes: Normal, Parkinson

    def forward(self, x):
        x = self.pool(F.relu(self.conv1(x)))
        x = x.view(-1, 16 * 112 * 112)
        x = self.fc1(x)
        return x

model = ParkinsonCNN()
torch.save(model, "parkinson_cnn.pth")
print("✅ Model saved as parkinson_cnn.pth")
