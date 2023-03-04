import cv2
import os
"""
在图中的指定位置画矩形
"""
masks_path = "image"
img = cv2.imread("./image/demo1.jpg")  # 此处以什么图像为准进行标记
print("请选择要标记的区域")
roi = cv2.selectROI(windowName="roi", img=img, showCrosshair=True, fromCenter=False)
x, y, w, h = roi
print('x:{0},y:{1},w:{2},h:{3}'.format(x, y, w, h))
# 开始画图
idx = 0
for img_item in os.listdir(masks_path):
    mask_path = os.path.join(masks_path, img_item)
    img = cv2.imread(mask_path)
    cv2.rectangle(img=img, pt1=(x, y), pt2=(x+w, y+h), color=(0, 0, 255), thickness=2)
    idx += 1
    cv2.imwrite("./out/{}.png".format(idx), img)
print("Finish")
