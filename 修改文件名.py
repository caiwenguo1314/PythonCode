#获取一个文件夹里所有文件的名称
#获取想要所有文件名中的关键字
#根据关键字将文件分类
#将所有文件按关键字存入含有关键字的文件夹中

# 导入os模块，用于处理文件和目录
import os
# 导入shutil模块，用于高级的文件操作，如复制、移动和删除文件
import shutil


# 定义一个函数，用于获取指定目录下的所有文件
def get_all_files_in_directory(directory):
    return os.listdir(directory)


# 定义一个函数，用于创建目录
def create_directory(directory):
    # 如果目录不存在
    if not os.path.exists(directory):
        # 创建目录
        os.makedirs(directory)


# 指定目录路径
directory = r'F:\20220507备份\2024项目\36立山23条路改造\立山路图\23条路投标版\PDF - 副本'  # 替换为你的文件夹路径

# 调用函数，获取目录下的所有文件
files = get_all_files_in_directory(directory)

# 遍历文件列表
for file in files:
    # 将文件名按照'-'分割成两部分
    parts = file.split('-')
    # 将目录和文件名拼接成新的文件名
    new_file_name = directory + '\\' + parts[0] + '-' + parts[1]
    # 创建新的目录
    create_directory(new_file_name)

    new_name = parts[0] + '-' + parts[1]    

    # 如果新文件名在文件中
    if new_name in file:
        # 源文件路径
        source = directory + '\\' + file
        # 目标文件路径
        destination = new_file_name
        # 移动文件
        shutil.move(source, destination)

# print(type(files))
# print(files[0])
