import cv2
import os


# 将分割的真实图转化二值图
def add_mask2image_binary(masks, masked):
    # Add binary masks to images
    for img_item in os.listdir(masks_path):
        mask_path = os.path.join(masks_path, img_item)
        mask = cv2.imread(mask_path, -1)
        res, masked = cv2.threshold(mask, 0, 255, cv2.THRESH_BINARY)
        cv2.imwrite(os.path.join(masked_path, img_item), masked)
    print("Finish")


# 注意使用全局路径，且无中文
masks_path = "../data/GT"          # 转换路径
masked_path = "../data/GT_binary"  # 保存路径
add_mask2image_binary(masks_path, masked_path)







