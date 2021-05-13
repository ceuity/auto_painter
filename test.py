# -*- conding: utf-8 -*-
import os
import time
import argparse

import tensorflow as tf
from PIL import Image
import numpy as np

from image_preprocessor import preprocess, denormalize
from auto_painter import load_auto_painter_model, generate_image

parser = argparse.ArgumentParser()

parser.add_argument('--path', default='./test.png', help='inference image path')

args = parser.parse_args()

# If you want to use GPU, Comment out this line.
os.environ["CUDA_VISIBLE_DEVICES"]="-1"

model = load_auto_painter_model()
IMG_WIDTH = 512
IMG_HEIGTH = 512

def load_image(filename):
  with open(filename, 'rb') as f:
    return np.array(f.read())

def test():
    curr_time = time.time()
    image_path = args.path
    source = load_image(image_path)
    adjusted_image = preprocess(source, IMG_WIDTH, IMG_HEIGTH)
    image = denormalize(adjusted_image)
    result = generate_image(model, adjusted_image)
    image = Image.fromarray(result)
    image_path = './images/'
    filename = 'result_image.png'
    image.save(image_path + filename)

if __name__ == '__main__':
    test()