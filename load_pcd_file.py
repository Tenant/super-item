'''
Using the following command to install pypcd

python3 -m pip install git+https://github.com/klintan/pypcd.git
'''

import numpy as np
from pypcd import pypcd

def load_pts(pcd):
  '''
  pcd: path of the pcd file
  points: numpy array containing the [x, y, z, intensity]
  '''
    pc_data = pypcd.PointCloud.from_path(pcd).pc_data
    scan = np.zeros((pc_data.shape[0], 4), dtype=np.float32)
    for i in range(pc_data.shape[0]):
        scan[i, 0] =  pc_data[i][1]
        scan[i, 1] = -pc_data[i][0]
        scan[i, 2] =  pc_data[i][2]
        scan[i, 3] =  pc_data[i][3]
    points = scan[:, 0:4]

    return points
