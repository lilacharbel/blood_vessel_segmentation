import cv2
import tifffile as tiff
import os
import matplotlib.pyplot as plt
from pyimagesearch import config
from imutils import paths
import numpy as np

# load
images_dir = sorted(list(paths.list_images(config.images_dir)))
masks_dir = sorted(list(paths.list_images(config.masks_dir)))

saved_images_dir = os.path.join('dataset', 'train', 'cropped_images')
saved_mask_dir = os.path.join('dataset', 'train', 'cropped_mask')

if not os.path.exists(saved_images_dir):
    os.makedirs(saved_images_dir)

if not os.path.exists(saved_mask_dir):
    os.makedirs(saved_mask_dir)


for img_dir, mask_dir in zip(images_dir, masks_dir):
    image = tiff.imread(img_dir)
    image = image[1, :, :]  # the green channel

    mask = cv2.imread(mask_dir, 0)
    mask[mask == 255] = 1

    clahe = cv2.createCLAHE(clipLimit=10.)
    final_img = clahe.apply(image)

    plt.figure()
    plt.imshow(final_img)
    plt.show()

    img_name = img_dir.split('\\')[-1].split('.')[0]
    images_names = [img_name+'_'+str(a) for a in range(4)]

    k = 0
    height, width = 600, 600
    for i in range(0, 1200, height):
        for j in range(0, 1200, width):
            croped_img = final_img[j:j+width, i:i+height]
            croped_mask = mask[j:j+width, i:i+height]

            np.save(os.path.join(saved_images_dir, images_names[k]), croped_img)
            np.save(os.path.join(saved_mask_dir, images_names[k]), croped_mask)

            k += 1

print(':)')