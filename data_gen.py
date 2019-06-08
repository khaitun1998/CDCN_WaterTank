import os, glob, sys
import numpy as np
import cv2

IMAGE_DIR = "./train/Train_image"
CROPPED_IMAGE_DIR = "./train/cropped_train_image"
MASK_DIR = "./Mask_Tank"
CROPPED_MASK_DIR = "./cropped_mask_tank"
tmp_file = "hoankiem"

paths = glob.glob(os.path.join(IMAGE_DIR, "**.jpg"))
tmp = 0
for path in paths:
    print(f"Processing image from {path}")
    basename = os.path.basename(path)
    filename = os.path.splitext(basename)[0]
    image = cv2.imread(path)
    image = cv2.resize(
        image, 
        (int(image.shape[1]//100)*100,
        int(image.shape[0]//100)*100)
    )
    cnt = 0
    for i in range(image.shape[0]//100):
        for j in range(image.shape[1]//100):
            temp2 = 0
            out = os.path.join(CROPPED_IMAGE_DIR, f"{tmp_file}_{tmp}.jpg")
            cv2.imwrite(out, image[i*100:(i+1)*100, j*100:(j+1)*100])
            cnt += 1
            tmp += 1
    print(f"Cropped into {cnt} images")

paths = glob.glob(os.path.join(MASK_DIR, "**.png"))
tmp1 = 0
for path in paths:
    print(f"Processing image from {path}")
    basename = os.path.basename(path)
    filename = os.path.splitext(basename)[0]
    image = cv2.imread(path)
    image = cv2.resize(
        image,
        (int(image.shape[1]//100)*100,
        int(image.shape[0]//100)*100)
    )
    cnt = 0
    for i in range(image.shape[0]//100):
        for j in range(image.shape[1]//100):
            out = os.path.join(CROPPED_MASK_DIR, f"{tmp_file}_{tmp1}_tank.png")
            cv2.imwrite(out, image[i*100:(i+1)*100, j*100:(j+1)*100])
            cnt += 1
            tmp1 += 1
    print(f"Cropped into {cnt} images")