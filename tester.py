
import numpy as np
from datetime import datetime 
import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
from torchvision import datasets, transforms
import matplotlib.pyplot as plt
import pandas as pd
from skimage import io, transform
import matplotlib.pyplot as plt
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms, utils
# Ignore warnings
import warnings
warnings.filterwarnings("ignore")
  
plt.ion()   # interactive mode
# check device
device = ("cuda" if torch.cuda.is_available() else "cpu")

"""This will be very epic and poggers"""



from torch.utils.data import Dataset
import pandas as pd
import os
import torchvision
from PIL import Image
import torch
from epichackathondetector import CNN
PATHz = "C:/Users/msajid/Desktop/pogmachinelearning/test"
model = torch.load(PATHz)
transform = transforms.Compose(
        [
            transforms.Resize((1000, 1000)),
            transforms.RandomCrop((950, 950)),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
        ]
    )
import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

if __name__ == "__main__":
    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

def on_created(event):
    img = Image.open(str(event.src_path)).convert("RGB")
    print("object detected")
    print("img name", event.src_path)
my_event_handler.on_created = on_created
path = "C:/Users/msajid/Desktop/pogmachinelearning"
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)
my_observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
img = transform(img)
label=0
y_label = torch.tensor(float(label))
img = img.unsqueeze(0)
with torch.no_grad():
  model.eval()
  img = img.to(device=device)
  y = y_label.to(device=device)
  pred = model(img)
  print(pred)
  predictions = torch.tensor([1.0 if i >= 0.52 else 0.0 for i in pred]).to(device)
  print(predictions)