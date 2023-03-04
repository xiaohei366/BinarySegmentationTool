import matplotlib.pyplot as plt
import numpy as np
"""
画散点图--比较性能和参数的关系
"""

# 定义画散点图的函数
def draw_scatter(n, s):
    """
    :param n: 点的数量，整数
    :param s:点的大小，整数
    :return: None
    """
    # 加载数据
    miou = [73.20, 74.81, 77.43, 76.39, 77.23, 79.19]
    params = [22.70, 51.45, 47.53, 31.04, 21.64, 12.62]
    # 通过切片获取横坐标x1
    x1 = params
    # 通过切片获取纵坐标R
    y1 = miou
    # 创建画图窗口
    fig = plt.figure()
    # 将画图窗口分成1行1列，选择第一块区域作子图
    ax1 = fig.add_subplot(1, 1, 1)
    # # 设置标题
    # ax1.set_title('Result Analysis')
    # 设置横坐标名称
    ax1.set_xlabel('Params/M')
    # 设置纵坐标名称
    ax1.set_ylabel('mIOU/%')
    # 画散点图
    ax1.scatter(x1, y1, s=s, c="#66B2FF", marker='D')
    # # 调整横坐标的上下界
    plt.ylim(ymax=80, ymin=72)
    # 显示
    plt.show()


# 主模块
if __name__ == "__main__":
    # 运行
    draw_scatter(n=2, s=200)