from random import choice
import os


def load_file():
    # 获取当前文件路径
    current_path = os.path.abspath(__file__)
    # 获取当前文件的父目录
    father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + ".")
    abs_path = father_path + "/img/"
    return abs_path

def rand_get():
    filePath = load_file()
    file_list = os.listdir(filePath)
    img_path=load_file()+choice(file_list)
    return img_path