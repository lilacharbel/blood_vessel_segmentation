import torch
import os

data_dir = os.path.join('dataset', 'train')
images_dir = os.path.join(data_dir, 'images')
masks_dir = os.path.join(data_dir, 'masks')

test_split = 0.15

device = 'cuda' if torch.cuda.is_available() else 'cpu'
pin_memory = True if device == 'cuda' else False

num_channels = 1
num_classes = 1
num_levels = 3

init_lr = 0.0001
epochs = 40
batch_size = 8

input_image_h = 1200
input_image_w = 1920

threshold = 0.3

output_dir = 'output'

test_images_dir = 'images_paths.txt'
test_masks_dir = 'masks_paths.txt'

pred_images_dir = os.path.join('dataset', 'data_for_segmentation')