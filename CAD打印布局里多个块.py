import pythoncom
import win32com.client
import time

# 启动 AutoCAD
acad = win32com.client.Dispatch("AutoCAD.Application.24")
doc = acad.ActiveDocument

# 初始化块计数器
block_count = 1
acad.ActiveDocument.SendCommand("FILEDIA 0\n")
acad.ActiveDocument.SendCommand("CMDDIA 0\n")

# 遍历所有块引用
for entity in doc.PaperSpace:
    if entity.EntityName == 'AcDbBlockReference' and entity.EffectiveName == 'A3图戳':
        # 获取块的边界框
        min_point, max_point = entity.GetBoundingBox()

        # 左下角和右上角坐标
        # print(f"块的左下角坐标: {min_point}")
        # print(f"块的右上角坐标: {max_point}")

        # 为每个块生成不同的PDF文件名
        pdf_path = f"C:\\Users\\Administrator\\Desktop\\友爱南街_{block_count}.PDF"

        # 禁用文件和命令对话框
       

        # 发送命令，将当前图纸输出为PDF文件
        acad.ActiveDocument.SendCommand(f"-plot\n"
                             "yes\n"  # 是否详细配置：是
                             "友爱南街\n"  # 布局：模型
                             "DWG To PDF.pc3\n"  # 打印设备                             
                             "ISO A3 (297.00 x 420.00 毫米)\n"  # 图纸尺寸
                             "M\n"
                             "landscape\n"  # 打印方向：横向
                             "no\n"  # 视图调整：不居中
                             "window\n"  # 选择打印窗口
                             f"{min_point[0]},{min_point[1]}\n"  # 窗口左下角
                             f"{max_point[0]},{max_point[1]}\n"  # 窗口右上角
                             "F\n"
                             "C\n"
                             "Y\n"
                             "monochrome.ctb\n"
                             "Y\n"
                             "Y\n"
                             "Y\n"
                             "Y\n"                             
                             f"{pdf_path}\n"  # 输出 PDF 文件路径
                             "Y\n"
                             "Y\n")

        # 恢复文件和命令对话框        
        
        # 增加块计数器，以便生成不同的PDF文件
        block_count += 1
        
        time.sleep(0.1)
acad.ActiveDocument.SendCommand("FILEDIA 1\n")
acad.ActiveDocument.SendCommand("CMDDIA 1\n")

print('打印结束')
