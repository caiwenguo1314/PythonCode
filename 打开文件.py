import os
import pyautogui
import time

# 替换下面的路径为你想要启动的.exe文件的实际路径
exe_path = r"D:\Tangent\TwtT20V9\TGStart.exe"

# 使用os.system方法启动.exe文件
# os.system(f'"{exe_path}"')
# 等待五秒
# time.sleep(10)
# 获取当前鼠标位置
x, y = pyautogui.position()

print(f"当前鼠标的位置是：X={x}, Y={y}")

pyautogui.click(x=81, y=12,clicks=2,interval=0.25)

# pyautogui.click(interval=0.25)
# pyautogui.moveTo(x=81, y=12, duration=1)  # 移动鼠标到指定位置
# pyautogui.sleep(1)  # 延时
# pyautogui.click()  # 执行点击

print(f"pyautogui执行了点击操作")
