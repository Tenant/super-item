import sys
import os

def walk_all_files_recursively(root_path, rela_path=".", file_list=[], dir_list=[]):
    #获取该目录下所有的文件名称和目录名称
    dir_or_files = os.listdir(os.path.join(root_path, rela_path))
    for dir_file in dir_or_files:
        #获取目录或者文件的路径
        dir_file_path = os.path.join(root_path, rela_path, dir_file)
        #判断该路径为文件还是路径
        if os.path.isdir(dir_file_path):
            #递归获取所有文件和目录的路径
            dir_list.append(os.path.join(rela_path, dir_file))
            walk_all_files_recursively(root_path, os.path.join(rela_path, dir_file), file_list=file_list, dir_list=dir_list)
        else:
            file_list.append(os.path.join(rela_path, dir_file))


if __name__ == '__main__':
    src =  sys.argv[1] # r"G:\KYXZ2020\G\考题数据\2018\OD\F\Raw-001"
    dst =  sys.argv[2] # r"G:\KYXZ2020\G\考题数据\2018\OD\L\Raw-001"
    if os.path.isdir(src):
        file_list = []
        dir_list = []
        walk_all_files_recursively(src, file_list=file_list, dir_list=dir_list)
        for dir in dir_list:
            os.makedirs(os.path.join(dst, dir), exist_ok=True)
        for file in file_list:
            cmd = "mklink /H " + os.path.join(dst, file) + " " + os.path.join(src, file) # mklink /H <destination> <source>
            os.system(cmd)
        else:
            cmd = "mklink /H " + dst + " " + src
            os.system(cmd)
