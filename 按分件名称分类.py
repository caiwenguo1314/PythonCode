#获取一个文件夹里所有文件的名称
#获取想要所有文件名中的关键字
#根据关键字将文件分类
#将所有文件按关键字存入含有关键字的文件夹中

# 导入os模块，用于处理文件和目录
import os
# 导入shutil模块，用于高级的文件操作，如复制、移动和删除文件
import shutil

directory = r'F:\20220507备份\2024项目\36立山23条路改造\23条路新返图纸'  # 替换为你的文件夹路径

new_name = '地形图'

new_file_name_new = directory + '\\' + '新版本'

new_file_name_old = directory + '\\' + '老版本'



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
# directory = r'F:\20220507备份\2024项目\36立山23条路改造\立山路图\23条路投标版\天正 - 副本'  # 替换为你的文件夹路径

# 调用函数，获取目录下的所有文件
files = get_all_files_in_directory(directory)

# 定义新文件名，路径为目录加上'老版本'
# new_file_name = directory + '\\' + '老版本'

# 定义新文件名，路径为目录加上'新版本'
# new_file_name1 = directory + '\\' + '新版本'

create_directory(new_file_name_new)


create_directory(new_file_name_old)


# new_name = '地形图'


for file in files:
    # 如果新文件名在文件中
    if new_name in file:
        # 源文件路径
        source = directory + '\\' +file
        # 目标文件路径
        destination = new_file_name_new
        # 移动文件
        shutil.move(source, destination)
    else:
        # 源文件路径
        source = directory + '\\' +file
        # 目标文件路径
        destination = new_file_name_old
        # 移动文件
        shutil.move(source, destination)

print('执行完毕')

# print(type(files))
# print(files[0])
