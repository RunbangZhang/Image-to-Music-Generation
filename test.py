from PyQt5.Qt import *
from model import DisentangleVAE
import torch
from quickdraw.names import *
import muspy
import pretty_midi
import os
import matplotlib.pyplot as plt
plt.switch_backend('Agg')
from torch.distributions import Normal
from amc_dl.torch_plus.train_utils import get_zs_from_dists
from PIL import Image
from PIL import ImageEnhance
from pr_visualization import *

import pygame
# mixer config
freq = 44100  # audio CD quality
bitsize = -16  # unsigned 16 bit
channels = 2  # 1 is mono, 2 is stereo
buffer = 1024  # number of samples
pygame.mixer.init(freq, bitsize, channels, buffer)

# optional volume 0 to 1.0
pygame.mixer.music.set_volume(1.0)
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = DisentangleVAE.init_model()
model.load_model("./result/models/disvae-nozoth_final.pt")
model.eval()


def listdir(path, list_name):
    for file in os.listdir(path):
        if file[-4:] == '.jpg' or file[-4:] == '.png':
            file_path = os.path.join(path, file)
            list_name.append(file_path)


styles = []
listdir('./resources/style_img', styles)

style_names = []
for style in styles:
    style_names.append(style.split('/')[-1].split('\\')[-1][:-4])


names = []
for category in QUICK_DRAWING_NAMES:
    if ' ' in category:
        names.append(category.replace(" ", '-'))
    else:
        names.append(category)
names.remove('circle')

for i, ch in enumerate(names):
    if ch == "marker":
        print(i)
