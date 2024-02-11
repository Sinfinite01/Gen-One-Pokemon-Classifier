import torch
import torch.nn as nn
import pandas as pd
import os
from torchvision import tranforms

class Net(nn.Module):
    def __init__(self):
        super().__init__()

        # nn layers