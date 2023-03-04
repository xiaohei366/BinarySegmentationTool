import cv2
import numpy as np
import os

# 重叠GT和原图像
def get_path(images_path, masks_path, visualized_path):
    for filename in os.listdir(images_path):
        img_path = os.path.join(images_path, filename)
        mask_path = os.path.join(masks_path, filename[:-4] + '.png')  # 此处可修改想要得到的图象格式
        img = cv2.imread(img_path, 1)
        mask = cv2.imread(mask_path, 0)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cv2.drawContours(img, contours, -1, (0, 0, 255), 1)
        img = img[:, :, ::-1]
        img[..., 2] = np.where(mask == 1, 255, img[..., 2])
        cv2.imwrite(os.path.join(visualized_path, filename), img)
        print("{} saved".format(filename))
    print("finish")


images_path = 'JPEGImages/'
masks_path = 'Annotations/'
visualized_path = 'visual/'
get_path(images_path, masks_path, visualized_path)