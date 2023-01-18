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
