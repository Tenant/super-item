'''
Assume that the label files end with '.csv', each label file has header and the label is the last element of each line
'''
import sys
import os

folder = "D:/Downloads/标注结果-zjk-data5"

dicts = {}
for f in os.listdir(folder):
    if f.endswith(".csv"):
        lines = [l.strip().split(",") for l in open(os.path.join(folder, f), 'r').readlines()[1:]] # skip the header
        for l in lines:
            k = int(l[-1]) # the last element of each line is its label
            if k in dicts.keys():
                dicts[k] += 1
            else:
                dicts[k] = 1
print(dicts)
