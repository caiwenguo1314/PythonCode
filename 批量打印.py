from pyautocad import Autocad, APoint
import time


acad = Autocad(create_if_not_exists=False)
acad.prompt("Hello, Autocad from Python\n")
print(acad.doc.Name)

# SendCommand


# 发送 -plot 命令，逐步输入选项并确认
acad.doc.SendCommand('-plot\n')  # 进入批处理打印命令
time.sleep(1)
acad.doc.SendCommand(' \n')
# # 打印设备，如 "DWG To PDF.pc3"
# acad.doc.SendCommand('DWG To PDF.pc3\n')

# # 页面设置，使用 "None"
# acad.doc.SendCommand('\n')

# # 打印范围，选择 Extents
# acad.doc.SendCommand('E\n')

# # 打印居中，选择 Yes
# acad.doc.SendCommand('Yes\n')

# # 打印比例，选择 1:1
# acad.doc.SendCommand('1:1\n')

# # 打印方向，选择 Portrait
# acad.doc.SendCommand('P\n')

# # 是否打印线宽，选择 Yes
# acad.doc.SendCommand('Yes\n')

# # 打印样式表，选择 monochrome.ctb
# acad.doc.SendCommand('monochrome.ctb\n')

# # 是否保存打印设置，选择 Yes
# acad.doc.SendCommand('Yes\n')

# # 是否打印，选择 Yes
# acad.doc.SendCommand('Yes\n')
