import numpy as np

scan = np.zeros((pc_data.shape[0], 4), dtype=np.float32)

# dump
scan.tofile(os.path.join(out_root, sequence, "velodyne", str(frame).zfill(6) + ".bin"))

# load
# has to specify the dtype or the wrong value will be loaded
pts = np.fromfile(os.path.join(out_root, sequence, "velodyne", str(frame).zfill(6) + ".bin"), dtype=np.float32).reshape(-1,4)
