import sys
import os
import numpy as np
import cv2

def construct_R(rot_x=0, rot_y=0, rot_z=0):
    sa, ca = np.sin(rot_x), np.cos(rot_x)
    sb, cb = np.sin(rot_y), np.cos(rot_y)
    sg, cg = np.sin(rot_z), np.cos(rot_z)
    cc_r1 = cb * cg
    cc_r2 = cg * sa * sb - ca * sg
    cc_r3 = sa * sg + ca * cg * sb
    cc_r4 = cb * sg
    cc_r5 = sa * sb * sg + ca * cg
    cc_r6 = ca * sb * sg - cg * sa
    cc_r7 = -sb
    cc_r8 = cb * sa
    cc_r9 = ca * cb
    return np.array([cc_r1, cc_r2, cc_r3, cc_r4, cc_r5, cc_r6, cc_r7, cc_r8, cc_r9]).reshape(3,3)

def transform_local_to_cam(xyz_local, r_cam, t_cam):
    '''
    convert points from local coordinate to camera cooridnate
    xyz_v - [[x], [y], [z]], np.array, 1x3
    r_vc  - [[r1, r2, r3], [r4, r5, r6], [r7, r8, r9]], np.array, 3x3
    t_vc  - [[t1], [t2], [t3]], np.array, 1x3
    '''
    xyz_cam = xyz_local - t_cam
    # r_cam_inv = np.linalg.inv(r_cam)
    r_cam_inv = r_cam
    xyz_cam = np.matmul(r_cam_inv, xyz_cam)
    return xyz_cam

def transform_cam_to_img(xyz_cam):
    '''
    convert points from camera coordinate to image coordinate
    K - [[fu, 0, cu], 
         [0, fv, cv], 
         [0, 0, 1]]
    '''
    cc_f = 20.513754829 # unit: mm
    cp_dpx = 0.023
    cp_dpy = 0.023
    cp_Cx = 512.14658869
    cp_Cy = 384.83460355
    xyz_uni = 1000 * xyz_cam / xyz_cam[2] * cc_f
    xyz_dis = xyz_uni[:2]
    Xf = xyz_dis[0] / cp_dpx + cp_Cx
    Yf = xyz_dis[1] / cp_dpy +  cp_Cy
    return [Xf, Yf]

def transform_local_to_image(xyz_local, r_cam, t_cam):
    xyz_cam = transform_local_to_cam(xyz_local, r_cam, t_cam)
    xy_img = transform_cam_to_img(xyz_cam)
    return xy_img

if __name__ == '__main__':
    R0 = construct_R(rot_x=0, rot_y=0, rot_z=3.35) # 3.45
    t0 = np.array([0.00, 1.12, 2.46]).reshape(3,1) # 0, 1.12 2.46
    R = construct_R(rot_x=1.5690272693, rot_y=-0.021000000, rot_z=0.0000000000)
    t = np.array([0, 1.760, 1.877]).reshape(3,1)

    root = r"G:/poss_odom/dataset"
    frame = 0
    img = cv2.imread(os.path.join(root, "sequences/00", "image_2", str(frame).zfill(6) + ".png"), -1)
    pts = np.fromfile(os.path.join(root, "sequences/00", "velodyne", str(frame).zfill(6) + ".bin"), dtype=np.float32).reshape(-1,4)
    for pt in pts:
        pt = pt[:3].reshape(3, 1)
        pt =  np.matmul(R0, pt) + t0
        [ix, iy] = (list(map(int, transform_local_to_image(pt, R, t)))) 
        iy = img.shape[0] - 1 - iy
        if 0 < ix < img.shape[1] and 0 < iy < img.shape[0]:
            img[iy][ix][0], img[iy][ix][1], img[iy][ix][2] = 0, 0, 255
    
    print("=" * 30)
    print("Transform matrix is:")
    T = np.zeros((4,4))
    T[:3, :3] = np.matmul(R, R0)
    T[:3, 3] = np.matmul(R, t0).reshape(-1) - t.reshape(-1)
    T[3, 3] = 1
    print(T)
    cv2.imshow("ss", img)
    cv2.waitKey(0)
