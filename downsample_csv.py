import sys

if __name__ == "__main__":
    fn = sys.argv[1]
    step = 100
    if len(sys.argv) > 2:
        step = int(sys.argv[2])
    raw_info = open(fn, "r").readlines()
    cnt = 0
    with open(fn[:-4] + "_downsample.csv", "w") as f:
        for i in range(0, len(raw_info), step):
            f.write(raw_info[i].strip() + "\n")
            cnt += 1
    print("downsample from {} to {} with step = {}".format(len(raw_info), cnt, step))