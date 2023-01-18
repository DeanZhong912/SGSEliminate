
# 获取手机截图
import subprocess
import cv2


def adb(order):
        return subprocess.Popen(order, shell=True, stdout=subprocess.PIPE, encoding='UTF-8').stdout

def get_screenshot():
    adb('adb shell /system/bin/screencap -p /sdcard/screenshot.jpg') # 将截图保存到SDCard
    adb('adb pull /sdcard/screenshot.jpg ./')# 将截图从手机拉取到电脑
    adb('adb shell rm /sdcard/screenshot.jpg')# 删除手机端的截图

    image = cv2.imread('./screenshot.jpg') # 使用imread读取截图

    return image

get_screenshot()

# 截图
from PIL import Image
import matplotlib.pyplot as plt

def image_cut_save(path, left, upper, right, lower, save_path):
    img = Image.open(path).convert("RGB")  # 打开图像
    box = (left, upper, right, lower)
    roi = img.crop(box)

    # 保存截取的图片
    roi.save(save_path)

#获得目标区域
pic_path = './screenshot.jpg'
pic_save_dir_path = './ocrTarget.jpg'
left, upper, right, lower = 46, 900, 1100, 2000
image_cut_save(pic_path, left, upper, right, lower, pic_save_dir_path)

