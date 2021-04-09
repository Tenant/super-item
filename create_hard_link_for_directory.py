# mklink /H <destination> <source>
import sys
import os

if __name__ == '__main__':
    src = r"G:\KYXZ2020\G\data\data_20201011\data-2\2020-10-11-11-36-51" # sys.argv[1]
    dst = r"G:\KYXZ2020\G\考题数据\2020\Raw-001\Raw-001-Camera" # sys.argv[2]
    files = os.listdir(src)
    for file in files:
        cmd = "mklink /H " + os.path.join(dst, file) + " " + os.path.join(src, file)
        os.system(cmd)
