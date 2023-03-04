import numpy as np
import  cv2
from PIL import Image
from os.path import join
import torch
import glob
"""
计算MIOU
"""

def compute_mIoU(gt_name_list, data_name_list):#计算mIoU的函数
    """
    Compute IoU given the predicted colorized images and
    """
    tp = 0
    fp = 0
    fn = 0
    tn = 0
    for ind in range(len(gt_name_list)):    # 读取每一个（图片-标签）对
        eps = 1e-5
        # 读取一张图像分割结果，转化成numpy数组（bool类型）
        prediction = np.array(Image.open(data_name_list[ind]).convert('1'), dtype=np.uint8)
        # 读取一张对应的标签，转化成numpy数组
        groundtruth = np.array(Image.open(gt_name_list[ind]), dtype=np.uint8)
        tp += np.sum((prediction == 1) & (groundtruth == 1))
        fp += np.sum((prediction == 1) & (groundtruth == 0))
        fn += np.sum((prediction == 0) & (groundtruth == 1))
        tn += np.sum((prediction == 0) & (groundtruth == 0))

        accuracy = (tp + tn) / (tp + tn + fp + fn + eps)
        precision = tp/ (tp + fp + eps)
        recall = tp / (tp + fn + eps)
        MIOU = (0.5*tp/(tp+fp+fn+eps)+0.5*tn/(tn+fp+fn+eps))
    print('accuracy', int(accuracy*100), '%')
    print('precision', int(precision*100), '%')
    print('recall', int(recall*100), '%')
    print('MIOU', int(MIOU*100), '%')

def main(data_dir, gt_dir):
    gt_name_list = glob.glob(gt_dir + '/' + '*.png')  # get the ground truth file name list
    data_name_list = glob.glob(data_dir + '/' + '*.png')  # get the ground truth file name list
    compute_mIoU(gt_name_list, data_name_list)   # 最后一个是分类数目



if __name__ == "__main__":
    data_dir = 'data/mass_road'  # 此处放预测数据
    gt_dir = 'data/GT'  # 此处放真实数据
    main(data_dir, gt_dir)